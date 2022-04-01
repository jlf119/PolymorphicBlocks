package edg.wir

import edgir.common.common
import edgir.elem.elem
import edgir.expr.expr
import edgir.init.init
import edgir.ref.ref
import edg.util.SeqMapSortableFrom._
import edgir.ref.ref.LibraryPath

import scala.collection.mutable


sealed trait BlockLike extends Pathable {
  def toPb: elem.BlockLike
}

/**
  * "Wrapper" around a HierarchyBlock. Sub-trees of blocks and links are contained as a mutable map in this object
  * (instead of the proto), while everything else is kept in the proto.
  * BlockLike / LinkLike lib_elem are kept in the proto, unmodified.
  * This is to allow efficient transformation at any point in the design tree without re-writing the root.
  */
class Block(pb: elem.HierarchyBlock, unrefinedType: Option[ref.LibraryPath]) extends BlockLike
    with HasMutablePorts with HasMutableBlocks with HasMutableLinks with HasMutableConstraints with HasParams {
  private val nameOrder = ProtoUtil.getNameOrder(pb.meta)
  override protected val ports: mutable.SeqMap[String, PortLike] = parsePorts(pb.ports, nameOrder)
  override protected val blocks: mutable.SeqMap[String, BlockLike] = parseBlocks(pb.blocks, nameOrder)
  override protected val links: mutable.SeqMap[String, LinkLike] = parseLinks(pb.links, nameOrder)
  override protected val constraints: mutable.SeqMap[String, expr.ValueExpr] = parseConstraints(pb.constraints, nameOrder)

  override def isElaborated: Boolean = true

  def getBlockClass: LibraryPath = pb.getSelfClass

  override def getParams: Map[String, init.ValInit] = pb.params

  override def resolve(suffix: Seq[String]): Pathable = suffix match {
    case Seq() => this
    case Seq(subname, tail@_*) =>
      if (ports.contains(subname)) {
        ports(subname).resolve(tail)
      } else if (blocks.contains(subname)) {
        blocks(subname).resolve(tail)
      } else if (links.contains(subname)) {
        links(subname).resolve(tail)
      } else {
        throw new InvalidPathException(s"No element $subname in Block")
      }
  }

  def toEltPb: elem.HierarchyBlock = {
    pb.copy(
      prerefineClass=unrefinedType match {
        case None => pb.prerefineClass
        case Some(prerefineClass) => Some(prerefineClass)
      },
      ports=ports.view.mapValues(_.toPb).toMap,
      blocks=blocks.view.mapValues(_.toPb).toMap,
      links=links.view.mapValues(_.toPb).toMap,
      constraints=constraints.toMap,
    )
  }

  override def toPb: elem.BlockLike = {
    elem.BlockLike(`type`=elem.BlockLike.Type.Hierarchy(toEltPb))
  }
}

// A generator version of the base block that can expand the block internals from a generator, subject to
// some constraints
class Generator(basePb: elem.HierarchyBlock, unrefinedType: Option[ref.LibraryPath])
    extends Block(basePb, unrefinedType) {
  require(basePb.generator.isDefined)

  var generatedPb: Option[elem.HierarchyBlock] = None

  blocks.clear()
  links.clear()
  constraints.clear()

  // Apply the generated block on top of the generator stub, and returns the ports that have arrays newly defined
  def applyGenerated(pb: elem.HierarchyBlock): Seq[String] = {
    require(generatedPb.isEmpty, "can't generate twice")
    require(pb.generator.isEmpty, "generated can't define generators")

    // check that the generated block is consistent with the generator stub
    require(pb.getSelfClass == basePb.getSelfClass)
    require(pb.params == basePb.params)

    // expand port arrays that may be defined by the generator
    require(pb.ports.keySet == basePb.ports.keySet)
    val expandedPorts = pb.ports.flatMap { case (portName, portPb) => portPb.is match {
      case elem.PortLike.Is.Array(port) if port.contains.isPorts && !basePb.ports(portName).getArray.contains.isPorts =>
        val port = ports(portName).asInstanceOf[PortArray]
        require(!port.isElaborated)
        ports.put(portName, PortLike.fromLibraryPb(portPb))
        Some(portName)
      case _ => None
    } }

    val nameOrder = ProtoUtil.getNameOrder(pb.meta)
    require(blocks.isEmpty)
    require(links.isEmpty)
    require(constraints.isEmpty)
    blocks.addAll(parseBlocks(pb.blocks, nameOrder))
    links.addAll(parseLinks(pb.links, nameOrder))
    constraints.addAll(parseConstraints(pb.constraints, nameOrder))

    generatedPb = Some(pb)

    expandedPorts.toSeq
  }

  // returns a list of dependencies of this generator
  def getDependencies: Seq[ref.LocalPath] = {
    basePb.getGenerator.requiredParams
  }

  def getDependenciesPorts: Seq[ref.LocalPath] = {  // TODO remove me w/ refactoring
    basePb.getGenerator.requiredPorts
  }

  override def toEltPb: elem.HierarchyBlock = {
    generatedPb.getOrElse(basePb).copy(  // if the block did not generate, return the base w/ the generator field
      prerefineClass=unrefinedType match {
        case None => generatedPb.getOrElse(basePb).prerefineClass
        case Some(prerefineClass) => Some(prerefineClass)
      },
      ports=ports.view.mapValues(_.toPb).toMap,
      blocks=blocks.view.mapValues(_.toPb).toMap,
      links=links.view.mapValues(_.toPb).toMap,
      constraints=constraints.toMap,
    )
  }
}

case class BlockLibrary(target: ref.LibraryPath) extends BlockLike {
  def resolve(suffix: Seq[String]): Pathable = suffix match {
    case Seq() => this
    case _ => throw new InvalidPathException(s"Can't resolve into library $target")
  }
  def toPb: elem.BlockLike = elem.BlockLike(elem.BlockLike.Type.LibElem(target))
  override def isElaborated: Boolean = false
}
