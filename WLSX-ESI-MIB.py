# PySNMP SMI module. Autogenerated from smidump -f python WLSX-ESI-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 09:00:43 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaESIServerMode, ArubaESIServerStatus, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaESIServerMode", "ArubaESIServerStatus")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Objects

wlsxESIMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10)).setRevisions(("1910-01-26 18:06",))
if mibBuilder.loadTexts: wlsxESIMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxESIMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089	\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxESIMIB.setDescription("This MIB module defines MIB objects which provide\ninformation about the External Services Interface (ESI) in the \n		Aruba controller.")
wlsxESIConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1))
wlsxESIServerTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1))
if mibBuilder.loadTexts: wlsxESIServerTable.setDescription("\nThis table lists all ESI servers configured on the controller.")
wlsxESIServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1)).setIndexNames((0, "WLSX-ESI-MIB", "esiServerName"))
if mibBuilder.loadTexts: wlsxESIServerEntry.setDescription("ESI Server Entry")
esiServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: esiServerName.setDescription("The name of the ESI Server")
esiServerGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerGroup.setDescription("The name of the ESI server group to which this server belongs.")
esiServerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 3), ArubaESIServerMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerMode.setDescription("The mode of this server")
esiServerTrustedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedIP.setDescription("The trusted IP address of this server, or 0.0.0.0 if it is not set")
esiServerUntrustedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedIP.setDescription("\nThe untrusted IP address of this server, or 0.0.0.0 if it is \nnot set")
esiServerTrustedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedSlot.setDescription("The slot number of the trusted interface for this server.")
esiServerTrustedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedPort.setDescription("The port number of the trusted interface for this server.")
esiServerUntrustedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedSlot.setDescription("The slot number of the untrusted interface for this server.")
esiServerUntrustedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedPort.setDescription("The port number of the untrusted interface for this server.")
esiServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 10), ArubaESIServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerStatus.setDescription("Indicates the status of this ESI server.")
esiServerTrustedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedModule.setDescription("The module number of the trusted interface for this server.")
esiServerUntrustedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedModule.setDescription("The module number of the untrusted interface for this server.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-ESI-MIB", PYSNMP_MODULE_ID=wlsxESIMIB)

# Objects
mibBuilder.exportSymbols("WLSX-ESI-MIB", wlsxESIMIB=wlsxESIMIB, wlsxESIConfigGroup=wlsxESIConfigGroup, wlsxESIServerTable=wlsxESIServerTable, wlsxESIServerEntry=wlsxESIServerEntry, esiServerName=esiServerName, esiServerGroup=esiServerGroup, esiServerMode=esiServerMode, esiServerTrustedIP=esiServerTrustedIP, esiServerUntrustedIP=esiServerUntrustedIP, esiServerTrustedSlot=esiServerTrustedSlot, esiServerTrustedPort=esiServerTrustedPort, esiServerUntrustedSlot=esiServerUntrustedSlot, esiServerUntrustedPort=esiServerUntrustedPort, esiServerStatus=esiServerStatus, esiServerTrustedModule=esiServerTrustedModule, esiServerUntrustedModule=esiServerUntrustedModule)

