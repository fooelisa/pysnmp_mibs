# PySNMP SMI module. Autogenerated from smidump -f python VPLS-BGP-DRAFT-01-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:57 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxExperiment, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxExperiment")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "transmission")
( RowStatus, StorageType, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention")
( jnxVplsConfigIndex, jnxVplsPwBindIndex, ) = mibBuilder.importSymbols("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex", "jnxVplsPwBindIndex")

# Objects

jnxVplsBgpDraft01MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 10)).setRevisions(("2006-12-06 12:00",))
if mibBuilder.loadTexts: jnxVplsBgpDraft01MIB.setOrganization("Layer 2 Virtual Private Networks (L2VPN) \nWorking  Group")
if mibBuilder.loadTexts: jnxVplsBgpDraft01MIB.setContactInfo("  \nV. J. Shah  \nEmail: vshah@juniper.net  \n\nThe L2VPN Working Group (email distribution l2vpn@ietf.org,  \nhttp://www.ietf.org/html.charters/l2vpn-charter.html)  ")
if mibBuilder.loadTexts: jnxVplsBgpDraft01MIB.setDescription("Copyright (C) The IETF Trust (2010). The initial  \nversion of this MIB module was published in RFC XXXX.  \n-- RFC Editor: Please replace XXXX with RFC number & remove \n--                    this note.  \n\nFor full legal notices see the RFC itself or see: \nhttp://www.ietf.org/copyrights/ianamib.html \n\nThis MIB module contains managed object definitions for   \nBGP signalled Virtual Private LAN Services as in \n[RFC4761]\n\nThis MIB module enables the use of any underlying PseudoWire \nnetwork. ")
jnxVplsBgpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1))
jnxVplsBgpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 1))
if mibBuilder.loadTexts: jnxVplsBgpConfigTable.setDescription("This table specifies information for configuring\nand monitoring BGP specific parameters for \nVirtual Private Lan Services(VPLS).")
jnxVplsBgpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 1, 1)).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"))
if mibBuilder.loadTexts: jnxVplsBgpConfigEntry.setDescription("A row in this table represents BGP specific information \nfor Virtual Private Lan Service(VPLS) in a packet network. \nIt is indexed by jnxVplsConfigIndex, which uniquely \nidentifies a single instance of a VPLS service.   \n\nA row is automatically created when a VPLS service is \nconfigured using BGP signalling.\n\nNone of the read-create objects values can be \nchanged when jnxVplsRowStatus is in the active(1) \nstate. Changes are allowed when the jnxVplsRowStatus \nis in notInService(2) or notReady(3) states only.   \nIf the operator need to change one of the values \nfor an active row the jnxVplsConfigRowStatus should be \nfirst changed to notInService(2), the objects may \nbe changed now, and later to active(1) in order to \nre-initiate the signaling process with the new \nvalues in effect.  ")
jnxVplsBgpConfigVERangeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpConfigVERangeSize.setDescription("Specifies the size of the range of VE ids in this \nVPLS service. This number controls the size of the \nlabel block advertised for this VE by the PE.  \nA value of 0 indicates that the range is not \nconfigured and the PE derives the range value \nfrom received advertisements from other PEs.")
jnxVplsBgpVETable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2))
if mibBuilder.loadTexts: jnxVplsBgpVETable.setDescription("This table associates VPLS Edge devices to a VPLS service")
jnxVplsBgpVEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1)).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"), (0, "VPLS-BGP-DRAFT-01-MIB", "jnxVplsBgpVEId"))
if mibBuilder.loadTexts: jnxVplsBgpVEEntry.setDescription("An entry in this table is created for each VE Id \nconfigured on a PE for a particular VPLS service \ninstance.")
jnxVplsBgpVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxVplsBgpVEId.setDescription("A secondary index identifying a VE within an\ninstance of a VPLS service.")
jnxVplsBgpVEName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 2), SnmpAdminString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpVEName.setDescription("Descriptive name for the site or u-PE assciated with \nthis VE Id.")
jnxVplsBgpVEPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpVEPreference.setDescription("Specifies the preference of the VE Id on this PE \nif the site is multi-homed and VE Id is re-used.")
jnxVplsBgpVERowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 5), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpVERowStatus.setDescription("This variable is used to create, modify, and/or\ndelete a row in this table.  When a row in this\ntable is in active(1) state, no objects in that row\ncan be modified except jnxVplsBgpSiteRowStatus.")
jnxVplsBgpVEStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 6), StorageType().clone('volatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpVEStorageType.setDescription("This variable indicates the storage type for this row.")
jnxVplsBgpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3))
if mibBuilder.loadTexts: jnxVplsBgpPwBindTable.setDescription("This table provides BGP specific information for \nan association between a VPLS service and the \ncorresponding Pseudo Wires. A service can have more \nthan one Pseudo Wire association. Pseudo Wires are \ndefined in the pwTable.")
jnxVplsBgpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3, 1)).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"), (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"))
if mibBuilder.loadTexts: jnxVplsBgpPwBindEntry.setDescription("Each row represents an association between a \nVPLS instance and one or more Pseudo Wires \ndefined in the pwTable. Each index is unique \nin describing an entry in this table. However\nboth indexes are required to define the one \nto many association of service to pseudowire.\n\nAn entry in this table in instantiated only when\nBGP signalling is used to configure VPLS service.\n\nEach entry in this table provides BGP specific\ninformation for the VPlS represented by \njnxVplsConfigIndex.")
jnxVplsBgpPwBindLocalVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpPwBindLocalVEId.setDescription("Identifies the local VE that this Pseudo Wire\nis associated with.")
jnxVplsBgpPwBindRemoteVEId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsBgpPwBindRemoteVEId.setDescription("Identifies the remote VE that this Pseudo Wire\nis associated with.")
jnxVplsBgpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 10, 2))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("VPLS-BGP-DRAFT-01-MIB", PYSNMP_MODULE_ID=jnxVplsBgpDraft01MIB)

# Objects
mibBuilder.exportSymbols("VPLS-BGP-DRAFT-01-MIB", jnxVplsBgpDraft01MIB=jnxVplsBgpDraft01MIB, jnxVplsBgpObjects=jnxVplsBgpObjects, jnxVplsBgpConfigTable=jnxVplsBgpConfigTable, jnxVplsBgpConfigEntry=jnxVplsBgpConfigEntry, jnxVplsBgpConfigVERangeSize=jnxVplsBgpConfigVERangeSize, jnxVplsBgpVETable=jnxVplsBgpVETable, jnxVplsBgpVEEntry=jnxVplsBgpVEEntry, jnxVplsBgpVEId=jnxVplsBgpVEId, jnxVplsBgpVEName=jnxVplsBgpVEName, jnxVplsBgpVEPreference=jnxVplsBgpVEPreference, jnxVplsBgpVERowStatus=jnxVplsBgpVERowStatus, jnxVplsBgpVEStorageType=jnxVplsBgpVEStorageType, jnxVplsBgpPwBindTable=jnxVplsBgpPwBindTable, jnxVplsBgpPwBindEntry=jnxVplsBgpPwBindEntry, jnxVplsBgpPwBindLocalVEId=jnxVplsBgpPwBindLocalVEId, jnxVplsBgpPwBindRemoteVEId=jnxVplsBgpPwBindRemoteVEId, jnxVplsBgpConformance=jnxVplsBgpConformance)
