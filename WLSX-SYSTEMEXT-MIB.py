# PySNMP SMI module. Autogenerated from smidump -f python WLSX-SYSTEMEXT-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 09:00:44 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaActiveState, ArubaCardType, ArubaSwitchRole, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaActiveState", "ArubaCardType", "ArubaSwitchRole")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Objects

wlsxSystemExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2)).setRevisions(("1908-12-11 21:08",))
if mibBuilder.loadTexts: wlsxSystemExtMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxSystemExtMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxSystemExtMIB.setDescription("This MIB module defines MIB objects which provide\nSystem level information about the Aruba controller.")
wlsxSystemExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1))
wlsxSysExtSwitchIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchIp.setDescription("Controller IP as configured by the user. This IP address uniquely \nidentifies the controller.")
wlsxSysExtHostname = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtHostname.setDescription("Name of the controller.")
wlsxSysExtModelName = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtModelName.setDescription("Model Name of the controller.")
wlsxSysExtSwitchRole = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 4), ArubaSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchRole.setDescription("Role of this controller in the Aruba Domain.")
wlsxSysExtSwitchMasterIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchMasterIp.setDescription("\nSwitch IP of the master controller.")
wlsxSysExtSwitchDate = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxSysExtSwitchDate.setDescription("\nSystem notion of the local date and time of day.")
wlsxSysExtSwitchBaseMacaddress = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchBaseMacaddress.setDescription("\nThe Base MAC address of the controller.")
wlsxSysExtFanTrayAssemblyNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtFanTrayAssemblyNumber.setDescription("\nAssembly number of the Fan tray.")
wlsxSysExtFanTraySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtFanTraySerialNumber.setDescription("\nSerial number of the Fan tray")
wlsxSysExtInternalTemparature = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtInternalTemparature.setDescription("\nInternal temperature in the controller.")
wlsxSysExtLicenseSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLicenseSerialNumber.setDescription("\nThe license serial number of the controller.")
wlsxSysExtSwitchLicenseCount = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseCount.setDescription("\nThe number of licenses installed on the controller")
wlsxSysExtProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13))
if mibBuilder.loadTexts: wlsxSysExtProcessorTable.setDescription("\nThe table of processors contained by the controller.")
wlsxSysExtProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtProcessorID"))
if mibBuilder.loadTexts: wlsxSysExtProcessorEntry.setDescription("\nAn entry for one processor contained by the controller.")
sysExtProcessorID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtProcessorID.setDescription("\nProcessor Index.")
sysExtProcessorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtProcessorDescr.setDescription("\nDescription of the processor.")
sysExtProcessorLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtProcessorLoad.setDescription("\nThe average, over the last minute, of the percentage of\ntime that this processor was not idle.")
wlsxSysExtStorageTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14))
if mibBuilder.loadTexts: wlsxSysExtStorageTable.setDescription("\nThe table of Storage-devices contained by the controller.")
wlsxSysExtStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtStorageIndex"))
if mibBuilder.loadTexts: wlsxSysExtStorageEntry.setDescription("\nAn entry for one long-term storage device contained by the \ncontroller.")
sysExtStorageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtStorageIndex.setDescription("\nIndex into the table.")
sysExtStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("ram", 1), ("flashMemory", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageType.setDescription("\nType of the storage.")
sysExtStorageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageSize.setDescription("\nTotal size of the storage filesystem in MB.")
sysExtStorageUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageUsed.setDescription("\nUsed Storage in MB.")
sysExtStorageName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageName.setDescription("\nName of the storage filesystem.")
wlsxSysExtMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15))
if mibBuilder.loadTexts: wlsxSysExtMemoryTable.setDescription("\nThe memory status of the controller")
wlsxSysExtMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtMemoryIndex"))
if mibBuilder.loadTexts: wlsxSysExtMemoryEntry.setDescription("\nAn entry for one memory region on the controller.  Currently,\nonly the control processor memory is monitored.")
sysExtMemoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtMemoryIndex.setDescription("\nIndex into the table.")
sysExtMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemorySize.setDescription("\nTotal memory in KB.")
sysExtMemoryUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemoryUsed.setDescription("\nUsed memory in KB.")
sysExtMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemoryFree.setDescription("\nFree memory in KB.")
wlsxSysExtCardTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16))
if mibBuilder.loadTexts: wlsxSysExtCardTable.setDescription("\nThe table of Hardware modules in the controller.")
wlsxSysExtCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtCardSlot"))
if mibBuilder.loadTexts: wlsxSysExtCardEntry.setDescription("\nAn entry for one Hardware Module in the controller.")
sysExtCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtCardSlot.setDescription("\nSlot in which this card is located, offset by one.  For the user-visible\nslot number see sysExtCardUserSlot")
sysExtCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 2), ArubaCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardType.setDescription("\nType of the Card.")
sysExtCardNumOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfPorts.setDescription("\nNumber of data ports on the card.	")
sysExtCardNumOfFastethernetPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfFastethernetPorts.setDescription("\nNumber of Fastethernet ports on the card.")
sysExtCardNumOfGigPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfGigPorts.setDescription("\nNumber of Gigabit ethernet ports on the card.")
sysExtCardSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardSerialNo.setDescription("\nSerial number of the card.")
sysExtCardAssemblyNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardAssemblyNo.setDescription("\nAssembly Number of the card.")
sysExtCardManufacturingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardManufacturingDate.setDescription("\nCard manufacturing date.")
sysExtCardHwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardHwRevision.setDescription("\nHardware revision of the card.")
sysExtCardFpgaRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardFpgaRevision.setDescription("\nFpga revision number.")
sysExtCardSwitchChip = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardSwitchChip.setDescription("\nSwitching Chip version.")
sysExtCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 12), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardStatus.setDescription("\nStatus of the card.")
sysExtCardUserSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardUserSlot.setDescription("\nUser-visible (zero-based) slot number.")
wlsxSysExtFanTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17))
if mibBuilder.loadTexts: wlsxSysExtFanTable.setDescription("\nThe table of all supported fans in the controller. Not supported in Aruba 200/800 and 2400 controllers.")
wlsxSysExtFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtFanIndex"))
if mibBuilder.loadTexts: wlsxSysExtFanEntry.setDescription("\nAn entry for one fan.")
sysExtFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtFanIndex.setDescription("\nIndex into the table.")
sysExtFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 2), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtFanStatus.setDescription("\nStatus of the Fan.")
wlsxSysExtPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18))
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyTable.setDescription("\nThe table of all supported Power supplies in the controller. Not supported in Aruba 200, 800 and 2400 controllers.")
wlsxSysExtPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtPowerSupplyIndex"))
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyEntry.setDescription("\nAn entry for one power supply.")
sysExtPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtPowerSupplyIndex.setDescription("\nIndex into the table.")
sysExtPowerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 2), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtPowerSupplyStatus.setDescription("\nStatus of the power supply.")
wlsxSysExtSwitchListTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19))
if mibBuilder.loadTexts: wlsxSysExtSwitchListTable.setDescription("This Table will list all the controllers in the Aruba Domain.\nIt will be populated only on the master controller. Local controllers\nreturn empty table.")
wlsxSysExtSwitchListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtSwitchIPAddress"))
if mibBuilder.loadTexts: wlsxSysExtSwitchListEntry.setDescription("Switch List Entry")
sysExtSwitchIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtSwitchIPAddress.setDescription("\nIP Address of the controller.")
sysExtSwitchRole = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 2), ArubaSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchRole.setDescription("\nRole of the controller.")
sysExtSwitchLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchLocation.setDescription("\nLocation of the controller")
sysExtSwitchSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchSWVersion.setDescription("\nSoftware version the controller is running.")
sysExtSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 5), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchStatus.setDescription("\nStatus of the controller.")
sysExtSwitchName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchName.setDescription("\nHost name of the controller.")
sysExtSwitchSerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchSerNo.setDescription("\nSerial number of the controller.")
wlsxSysExtSwitchLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20))
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseTable.setDescription("This table lists all licenses installed on the controller.")
wlsxSysExtLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1)).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtLicenseIndex"))
if mibBuilder.loadTexts: wlsxSysExtLicenseEntry.setDescription("License Entry")
sysExtLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysExtLicenseIndex.setDescription("\nLicense ID number")
sysExtLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseKey.setDescription("\nLicense Key")
sysExtLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseInstalled.setDescription("\nLicense installation time")
sysExtLicenseExpires = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseExpires.setDescription("\nLicense expiry time")
sysExtLicenseFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseFlags.setDescription("\nLicense flags; E - enabled; A - auto-generated;\n               R - reboot required to activate")
sysExtLicenseService = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseService.setDescription("\nThe service enabled by this license.")
wlsxSysExtMMSCompatLevel = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMMSCompatLevel.setDescription("\nLists the compatibility level of this controller with the MMS")
wlsxSysExtMMSConfigID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMMSConfigID.setDescription("\nThis Object represents the value of the MMS Configuration ID in the controller.")
wlsxSysExtControllerConfigID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtControllerConfigID.setDescription("\nThis Object represents the value of the Controller's Configuration ID.")
wlsxSysExtIsMMSConfigUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 24), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxSysExtIsMMSConfigUpdateEnabled.setDescription("\nThis objects indicates whether the controller is configured to accept configuration snapshots from MMS.")
wlsxSysExtSwitchLastReload = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchLastReload.setDescription("\nThe reason for the last controller reload")
wlsxSysExtLastStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 26), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLastStatsReset.setDescription("\nLast time switch stats was reset")
wlsxSysExtHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtHwVersion.setDescription("Hardware version of the switch.")
wlsxSysExtSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwVersion.setDescription("Software version of the switch.")
wlsxSysExtSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSerialNumber.setDescription("The serial number of the switch.")
wlsxSysExtCpuUsedPercent = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 30), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtCpuUsedPercent.setDescription("The CPU used percent of the switch")
wlsxSysExtMemoryUsedPercent = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 31), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMemoryUsedPercent.setDescription("The memory used percent of the switch")
wlsxSysExtPacketLossPercent = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtPacketLossPercent.setDescription("The packet loss count of the switch")
wlsxSystemExtTableGenNumberGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2))
wlsxSysExtUserTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtUserTableGenNumber.setDescription("\nThis objects denotes the number of times the user table was \nmodified since reboot.")
wlsxSysExtAPBssidTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPBssidTableGenNumber.setDescription("\nThis objects denotes the number of times the AP BSSID table was \nmodified since reboot.")
wlsxSysExtAPRadioTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPRadioTableGenNumber.setDescription("\nThis objects denotes the number of times the Radio table was \nmodified since reboot.")
wlsxSysExtAPTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPTableGenNumber.setDescription("\nThis objects denotes the number of times the AP table was \nmodified since reboot.")
wlsxSysExtSwitchListTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchListTableGenNumber.setDescription("\nThis objects denotes the number of times the Switch list table was \nmodified since reboot.")
wlsxSysExtPortTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtPortTableGenNumber.setDescription("\nThis objects denotes the number of times the port table was \nmodified since reboot.")
wlsxSysExtVlanTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtVlanTableGenNumber.setDescription("\nThis objects denotes the number of times the Vlan table was \nmodified since reboot.")
wlsxSysExtVlanInterfaceTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtVlanInterfaceTableGenNumber.setDescription("\nThis objects denotes the number of times the Vlan Interface table \nwas modified since reboot.")
wlsxSysExtLicenseTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLicenseTableGenNumber.setDescription("\nThis objects denotes the number of times the license table\nwas modified since reboot.")
wlsxSysExtMonAPTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMonAPTableGenNumber.setDescription("\nThis objects denotes the number of times the monitored AP table\nwas modified since reboot.")
wlsxSysExtMonStationTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMonStationTableGenNumber.setDescription("\nThis objects denotes the number of times the monitored station table\nwas modified since reboot.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-SYSTEMEXT-MIB", PYSNMP_MODULE_ID=wlsxSystemExtMIB)

# Objects
mibBuilder.exportSymbols("WLSX-SYSTEMEXT-MIB", wlsxSystemExtMIB=wlsxSystemExtMIB, wlsxSystemExtGroup=wlsxSystemExtGroup, wlsxSysExtSwitchIp=wlsxSysExtSwitchIp, wlsxSysExtHostname=wlsxSysExtHostname, wlsxSysExtModelName=wlsxSysExtModelName, wlsxSysExtSwitchRole=wlsxSysExtSwitchRole, wlsxSysExtSwitchMasterIp=wlsxSysExtSwitchMasterIp, wlsxSysExtSwitchDate=wlsxSysExtSwitchDate, wlsxSysExtSwitchBaseMacaddress=wlsxSysExtSwitchBaseMacaddress, wlsxSysExtFanTrayAssemblyNumber=wlsxSysExtFanTrayAssemblyNumber, wlsxSysExtFanTraySerialNumber=wlsxSysExtFanTraySerialNumber, wlsxSysExtInternalTemparature=wlsxSysExtInternalTemparature, wlsxSysExtLicenseSerialNumber=wlsxSysExtLicenseSerialNumber, wlsxSysExtSwitchLicenseCount=wlsxSysExtSwitchLicenseCount, wlsxSysExtProcessorTable=wlsxSysExtProcessorTable, wlsxSysExtProcessorEntry=wlsxSysExtProcessorEntry, sysExtProcessorID=sysExtProcessorID, sysExtProcessorDescr=sysExtProcessorDescr, sysExtProcessorLoad=sysExtProcessorLoad, wlsxSysExtStorageTable=wlsxSysExtStorageTable, wlsxSysExtStorageEntry=wlsxSysExtStorageEntry, sysExtStorageIndex=sysExtStorageIndex, sysExtStorageType=sysExtStorageType, sysExtStorageSize=sysExtStorageSize, sysExtStorageUsed=sysExtStorageUsed, sysExtStorageName=sysExtStorageName, wlsxSysExtMemoryTable=wlsxSysExtMemoryTable, wlsxSysExtMemoryEntry=wlsxSysExtMemoryEntry, sysExtMemoryIndex=sysExtMemoryIndex, sysExtMemorySize=sysExtMemorySize, sysExtMemoryUsed=sysExtMemoryUsed, sysExtMemoryFree=sysExtMemoryFree, wlsxSysExtCardTable=wlsxSysExtCardTable, wlsxSysExtCardEntry=wlsxSysExtCardEntry, sysExtCardSlot=sysExtCardSlot, sysExtCardType=sysExtCardType, sysExtCardNumOfPorts=sysExtCardNumOfPorts, sysExtCardNumOfFastethernetPorts=sysExtCardNumOfFastethernetPorts, sysExtCardNumOfGigPorts=sysExtCardNumOfGigPorts, sysExtCardSerialNo=sysExtCardSerialNo, sysExtCardAssemblyNo=sysExtCardAssemblyNo, sysExtCardManufacturingDate=sysExtCardManufacturingDate, sysExtCardHwRevision=sysExtCardHwRevision, sysExtCardFpgaRevision=sysExtCardFpgaRevision, sysExtCardSwitchChip=sysExtCardSwitchChip, sysExtCardStatus=sysExtCardStatus, sysExtCardUserSlot=sysExtCardUserSlot, wlsxSysExtFanTable=wlsxSysExtFanTable, wlsxSysExtFanEntry=wlsxSysExtFanEntry, sysExtFanIndex=sysExtFanIndex, sysExtFanStatus=sysExtFanStatus, wlsxSysExtPowerSupplyTable=wlsxSysExtPowerSupplyTable, wlsxSysExtPowerSupplyEntry=wlsxSysExtPowerSupplyEntry, sysExtPowerSupplyIndex=sysExtPowerSupplyIndex, sysExtPowerSupplyStatus=sysExtPowerSupplyStatus, wlsxSysExtSwitchListTable=wlsxSysExtSwitchListTable, wlsxSysExtSwitchListEntry=wlsxSysExtSwitchListEntry, sysExtSwitchIPAddress=sysExtSwitchIPAddress, sysExtSwitchRole=sysExtSwitchRole, sysExtSwitchLocation=sysExtSwitchLocation, sysExtSwitchSWVersion=sysExtSwitchSWVersion, sysExtSwitchStatus=sysExtSwitchStatus, sysExtSwitchName=sysExtSwitchName, sysExtSwitchSerNo=sysExtSwitchSerNo, wlsxSysExtSwitchLicenseTable=wlsxSysExtSwitchLicenseTable, wlsxSysExtLicenseEntry=wlsxSysExtLicenseEntry, sysExtLicenseIndex=sysExtLicenseIndex, sysExtLicenseKey=sysExtLicenseKey, sysExtLicenseInstalled=sysExtLicenseInstalled, sysExtLicenseExpires=sysExtLicenseExpires, sysExtLicenseFlags=sysExtLicenseFlags, sysExtLicenseService=sysExtLicenseService, wlsxSysExtMMSCompatLevel=wlsxSysExtMMSCompatLevel, wlsxSysExtMMSConfigID=wlsxSysExtMMSConfigID, wlsxSysExtControllerConfigID=wlsxSysExtControllerConfigID, wlsxSysExtIsMMSConfigUpdateEnabled=wlsxSysExtIsMMSConfigUpdateEnabled, wlsxSysExtSwitchLastReload=wlsxSysExtSwitchLastReload, wlsxSysExtLastStatsReset=wlsxSysExtLastStatsReset, wlsxSysExtHwVersion=wlsxSysExtHwVersion, wlsxSysExtSwVersion=wlsxSysExtSwVersion, wlsxSysExtSerialNumber=wlsxSysExtSerialNumber, wlsxSysExtCpuUsedPercent=wlsxSysExtCpuUsedPercent, wlsxSysExtMemoryUsedPercent=wlsxSysExtMemoryUsedPercent, wlsxSysExtPacketLossPercent=wlsxSysExtPacketLossPercent, wlsxSystemExtTableGenNumberGroup=wlsxSystemExtTableGenNumberGroup, wlsxSysExtUserTableGenNumber=wlsxSysExtUserTableGenNumber, wlsxSysExtAPBssidTableGenNumber=wlsxSysExtAPBssidTableGenNumber, wlsxSysExtAPRadioTableGenNumber=wlsxSysExtAPRadioTableGenNumber, wlsxSysExtAPTableGenNumber=wlsxSysExtAPTableGenNumber, wlsxSysExtSwitchListTableGenNumber=wlsxSysExtSwitchListTableGenNumber, wlsxSysExtPortTableGenNumber=wlsxSysExtPortTableGenNumber, wlsxSysExtVlanTableGenNumber=wlsxSysExtVlanTableGenNumber, wlsxSysExtVlanInterfaceTableGenNumber=wlsxSysExtVlanInterfaceTableGenNumber, wlsxSysExtLicenseTableGenNumber=wlsxSysExtLicenseTableGenNumber, wlsxSysExtMonAPTableGenNumber=wlsxSysExtMonAPTableGenNumber, wlsxSysExtMonStationTableGenNumber=wlsxSysExtMonStationTableGenNumber)

