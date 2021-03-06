# PySNMP SMI module. Autogenerated from smidump -f python CISCO-SMI
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:34 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "enterprises")

# Objects

cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9)).setRevisions(("2012-08-29 00:00","2009-02-03 00:00","2002-03-21 00:00","2001-05-22 00:00","2000-11-01 22:46","2000-01-11 00:00","1997-04-09 00:00","1995-05-16 00:00","1994-04-26 20:00",))
if mibBuilder.loadTexts: cisco.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: cisco.setContactInfo("Cisco Systems\nCustomer Service\n\nPostal: 170 West Tasman Drive\nSan Jose, CA  95134\nUSA\n\nTel: +1 800 553-NETS\n\nE-mail: cs-snmp@cisco.com")
if mibBuilder.loadTexts: cisco.setDescription("The Structure of Management Information for the\nCisco enterprise.")
ciscoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 1))
if mibBuilder.loadTexts: ciscoProducts.setDescription("ciscoProducts is the root OBJECT IDENTIFIER from\nwhich sysObjectID values are assigned.  Actual\nvalues are defined in CISCO-PRODUCTS-MIB.")
local = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 2))
if mibBuilder.loadTexts: local.setDescription("Subtree beneath which pre-10.2 MIBS were built.")
temporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 3))
if mibBuilder.loadTexts: temporary.setDescription("Subtree beneath which pre-10.2 experiments were\nplaced.")
pakmon = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 4))
if mibBuilder.loadTexts: pakmon.setDescription("reserved for pakmon")
workgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 5))
if mibBuilder.loadTexts: workgroup.setDescription("subtree reserved for use by the Workgroup Business Unit")
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6))
if mibBuilder.loadTexts: otherEnterprises.setDescription("otherEnterprises provides a root object identifier\nfrom which mibs produced by other companies may be\nplaced.  mibs produced by other enterprises are\ntypicially implemented with the object identifiers\nas defined in the mib, but if the mib is deemed to\nbe uncontrolled, we may reroot the mib at this\nsubtree in order to have a controlled version.")
ciscoSB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1))
if mibBuilder.loadTexts: ciscoSB.setDescription("ciscoSB provides root Object Identifier for Management\nInformation Base for products of Cisco Small Business.\nThis includes products rebranded from linksys aquisition.\nMIB numbers under this root are managed and controlled\nby ciscosb_mib@cisco.com.")
ciscoSMB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 2))
if mibBuilder.loadTexts: ciscoSMB.setDescription("ciscoSMB provides root Object Identifier for Management\nInformation Base for products of Cisco built for Small and \nMedium Business market.The MIB numbers under this root are \nmanaged and controlled by ciscosmb_mib@cisco.com")
ciscoAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 7))
if mibBuilder.loadTexts: ciscoAgentCapability.setDescription("ciscoAgentCapability provides a root object identifier\nfrom which AGENT-CAPABILITIES values may be assigned.")
ciscoConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 8))
if mibBuilder.loadTexts: ciscoConfig.setDescription("ciscoConfig is the main subtree for configuration mibs.")
ciscoMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9))
if mibBuilder.loadTexts: ciscoMgmt.setDescription("ciscoMgmt is the main subtree for new mib development.")
ciscoExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10))
if mibBuilder.loadTexts: ciscoExperiment.setDescription("ciscoExperiment provides a root object identifier\nfrom which experimental mibs may be temporarily\nbased.  mibs are typicially based here if they\nfall in one of two categories\n1) are IETF work-in-process mibs which have not\nbeen assigned a permanent object identifier by\nthe IANA.\n2) are cisco work-in-process which has not been\nassigned a permanent object identifier by the\ncisco assigned number authority, typicially because\nthe mib is not ready for deployment.\n\nNOTE WELL:  support for mibs in the ciscoExperiment\nsubtree will be deleted when a permanent object\nidentifier assignment is made.")
ciscoAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11))
if mibBuilder.loadTexts: ciscoAdmin.setDescription("ciscoAdmin is reserved for administratively assigned\nOBJECT IDENTIFIERS, i.e. those not associated with MIB\nobjects")
ciscoProxy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 1))
if mibBuilder.loadTexts: ciscoProxy.setDescription("ciscoProxy OBJECT IDENTIFIERS are used to uniquely name\nparty mib records created to proxy for SNMPv1.")
ciscoPartyProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 1))
ciscoContextProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 2))
ciscoRptrGroupObjectID = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2))
if mibBuilder.loadTexts: ciscoRptrGroupObjectID.setDescription("ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to\nuniquely identify groups of repeater ports for use by the\nSNMP-REPEATER-MIB (RFC 1516) rptrGroupObjectID object.")
ciscoUnknownRptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 1))
if mibBuilder.loadTexts: ciscoUnknownRptrGroup.setDescription("The identity of an unknown repeater port group.")
cisco2505RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 2))
if mibBuilder.loadTexts: cisco2505RptrGroup.setDescription("The authoritative identity of the Cisco 2505 repeater\nport group.")
cisco2507RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 3))
if mibBuilder.loadTexts: cisco2507RptrGroup.setDescription("The authoritative identity of the Cisco 2507 repeater\nport group.")
cisco2516RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 4))
if mibBuilder.loadTexts: cisco2516RptrGroup.setDescription("The authoritative identity of the Cisco 2516 repeater\nport group.")
ciscoWsx5020RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 5))
if mibBuilder.loadTexts: ciscoWsx5020RptrGroup.setDescription("The authoritative identity of the wsx5020 repeater\nport group.")
ciscoChipSets = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3))
if mibBuilder.loadTexts: ciscoChipSets.setDescription("Numerous media-specific MIBS have an object, defined as\nan OBJECT IDENTIFIER, which is the identity of the chipset\nrealizing the interface.  Cisco-specific chipsets have their \nOBJECT IDENTIFIERS assigned under this subtree.")
ciscoChipSetSaint1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 1))
if mibBuilder.loadTexts: ciscoChipSetSaint1.setDescription("The identity of the Rev 1 SAINT ethernet chipset\nmanufactured for cisco by LSI Logic.")
ciscoChipSetSaint2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 2))
if mibBuilder.loadTexts: ciscoChipSetSaint2.setDescription("The identity of the Rev 2 SAINT ethernet chipset\nmanufactured for cisco by LSI Logic.")
ciscoChipSetSaint3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 3))
if mibBuilder.loadTexts: ciscoChipSetSaint3.setDescription("The identity of the Rev 3 SAINT ethernet chipset\nmanufactured for cisco by Plessey.")
ciscoChipSetSaint4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 4))
if mibBuilder.loadTexts: ciscoChipSetSaint4.setDescription("The identity of the Rev 4 SAINT ethernet chipset\nmanufactured for cisco by Mitsubishi.")
ciscoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 12))
if mibBuilder.loadTexts: ciscoModules.setDescription("ciscoModules provides a root object identifier\nfrom which MODULE-IDENTITY values may be assigned.")
lightstream = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 13))
if mibBuilder.loadTexts: lightstream.setDescription("subtree reserved for use by Lightstream")
ciscoworks = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 14))
if mibBuilder.loadTexts: ciscoworks.setDescription("ciscoworks provides a root object identifier beneath\nwhich mibs applicable to the CiscoWorks family of network\nmanagement products are defined.")
newport = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 15))
if mibBuilder.loadTexts: newport.setDescription("subtree reserved for use by the former Newport Systems\nSolutions, now a portion of the Access Business Unit.")
ciscoPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 16))
if mibBuilder.loadTexts: ciscoPartnerProducts.setDescription("ciscoPartnerProducts is the root OBJECT IDENTIFIER from\nwhich partner sysObjectID values may be assigned. Such \nsysObjectID values are composed of the ciscoPartnerProducts\nprefix, followed by a single identifier that is unique for \neach partner, followed by the value of sysObjectID of the\nCisco product from which partner product is derived.  Note\nthat the chassisPartner MIB object defines the value of the\nidentifier assigned to each partner.")
ciscoPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17))
if mibBuilder.loadTexts: ciscoPolicy.setDescription("ciscoPolicy is the root of the Cisco-assigned OID\nsubtree for use with Policy Management.")
ciscoPIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17, 2))
if mibBuilder.loadTexts: ciscoPIB.setDescription("ciscoPIB is the root of the Cisco-assigned OID\nsubtree for assignment to PIB (Policy Information\nBase) modules.")
ciscoPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18))
if mibBuilder.loadTexts: ciscoPolicyAuto.setDescription("ciscoPolicyAuto is the root of the Cisco-assigned\nOID subtree for OIDs which are automatically assigned\nfor use in Policy Management.")
ciscoPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18, 2))
if mibBuilder.loadTexts: ciscoPibToMib.setDescription("ciscoPibToMib is the root of the Cisco-assigned\nOID subtree for MIBs which are algorithmically\ngenerated/translated from Cisco PIBs with OIDs\nassigned under the ciscoPIB subtree.\nThese generated MIBs allow management\nentities (other the current Policy Server) to\nread the downloaded policy.  By convention, for PIB\n'ciscoPIB.x', the generated MIB shall have the\nname 'ciscoPibToMib.x'.")
ciscoDomains = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19))
if mibBuilder.loadTexts: ciscoDomains.setDescription("ciscoDomains provides a root object identifier from which\ndifferent transport mapping values may be assigned.")
ciscoTDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 19, 99999))
ciscoTDomainUdpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 1))
if mibBuilder.loadTexts: ciscoTDomainUdpIpv4.setDescription("The UDP over IPv4 transport domain.  The corresponding\ntransport address is of type CiscoTAddressIPv4.")
ciscoTDomainUdpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 2))
if mibBuilder.loadTexts: ciscoTDomainUdpIpv6.setDescription("The UDP over IPv6 transport domain.  The corresponding\ntransport address is of type CiscoTAddressIPv6 for global IPv6\naddresses and CiscoTAddressIPv6s for scoped IPv6 addresses.")
ciscoTDomainTcpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 3))
if mibBuilder.loadTexts: ciscoTDomainTcpIpv4.setDescription("The TCP over IPv4 transport domain.  The corresponding\ntransport address is of type CiscoTAddressIPv4.")
ciscoTDomainTcpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 4))
if mibBuilder.loadTexts: ciscoTDomainTcpIpv6.setDescription("The TCP over IPv6 transport domain.  The corresponding\ntransport address is of type CiscoTAddressIPv6 for global IPv6\naddresses and CiscoTAddressIPv6s for scoped IPv6 addresses.")
ciscoTDomainLocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 5))
if mibBuilder.loadTexts: ciscoTDomainLocal.setDescription("The Posix Local IPC transport domain. The corresponding\ntransport address is of type CiscoTAddressLocal.  The Posix\nLocal IPC transport domain incorporates the well known UNIX\ndomain sockets.")
ciscoTDomainClns = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 6))
if mibBuilder.loadTexts: ciscoTDomainClns.setDescription("The CLNS transport domain.  The corresponding transport\naddress is of type CiscoTAddressOSI.")
ciscoTDomainCons = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 7))
if mibBuilder.loadTexts: ciscoTDomainCons.setDescription("The CONS transport domain.  The corresponding transport\naddress is of type CiscoTAddressOSI.")
ciscoTDomainDdp = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 8))
if mibBuilder.loadTexts: ciscoTDomainDdp.setDescription("The DDP transport domain.  The corresponding transport\naddress is of type CiscoTAddressNBP.")
ciscoTDomainIpx = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 9))
if mibBuilder.loadTexts: ciscoTDomainIpx.setDescription("The IPX transport domain.  The corresponding transport\naddress is of type CiscoTAddressIPX.")
ciscoTDomainSctpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 10))
if mibBuilder.loadTexts: ciscoTDomainSctpIpv4.setDescription("The SCTP over IPv4 transport domain.  The corresponding\ntransport address is of type CiscoTAddressIPv4.")
ciscoTDomainSctpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 11))
if mibBuilder.loadTexts: ciscoTDomainSctpIpv6.setDescription("The SCTP over IPv6 transport domain.  The corresponding\ntransport address is of type CiscoTAddressIPv6 for global IPv6\naddresses and CiscoTAddressIPv6s for scoped IPv6 addresses.")
ciscoCIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20))
if mibBuilder.loadTexts: ciscoCIB.setDescription("ciscoCIB is the root of the Cisco-assigned OID subtree for\nassignment to MIB modules describing managed objects that\npart of the CPE automatic configuration framework.")
ciscoCibMmiGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 1))
if mibBuilder.loadTexts: ciscoCibMmiGroup.setDescription("ciscoCibMmiGroup is the root of the Cisco-assigned OID\nsubtree for assignment to MIB modules describing managed\nobjects supporting the Modem Management Interface (MMI),\nthe interface that facilitates CPE automatic configuration.")
ciscoCibProvGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 2))
if mibBuilder.loadTexts: ciscoCibProvGroup.setDescription("ciscoCibStoreGroup is the root of the Cisco-assigned OID\nsubtree for assignment to MIB modules describing managed\nobjects contributing to the Configuration Information Base\n(CIB).")
ciscoPKI = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 21))
if mibBuilder.loadTexts: ciscoPKI.setDescription("ciscoPKI is the root of cisco-assigned OID subtree for PKI\nCertificate Policies and Certificate Extensions.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-SMI", PYSNMP_MODULE_ID=cisco)

# Objects
mibBuilder.exportSymbols("CISCO-SMI", cisco=cisco, ciscoProducts=ciscoProducts, local=local, temporary=temporary, pakmon=pakmon, workgroup=workgroup, otherEnterprises=otherEnterprises, ciscoSB=ciscoSB, ciscoSMB=ciscoSMB, ciscoAgentCapability=ciscoAgentCapability, ciscoConfig=ciscoConfig, ciscoMgmt=ciscoMgmt, ciscoExperiment=ciscoExperiment, ciscoAdmin=ciscoAdmin, ciscoProxy=ciscoProxy, ciscoPartyProxy=ciscoPartyProxy, ciscoContextProxy=ciscoContextProxy, ciscoRptrGroupObjectID=ciscoRptrGroupObjectID, ciscoUnknownRptrGroup=ciscoUnknownRptrGroup, cisco2505RptrGroup=cisco2505RptrGroup, cisco2507RptrGroup=cisco2507RptrGroup, cisco2516RptrGroup=cisco2516RptrGroup, ciscoWsx5020RptrGroup=ciscoWsx5020RptrGroup, ciscoChipSets=ciscoChipSets, ciscoChipSetSaint1=ciscoChipSetSaint1, ciscoChipSetSaint2=ciscoChipSetSaint2, ciscoChipSetSaint3=ciscoChipSetSaint3, ciscoChipSetSaint4=ciscoChipSetSaint4, ciscoModules=ciscoModules, lightstream=lightstream, ciscoworks=ciscoworks, newport=newport, ciscoPartnerProducts=ciscoPartnerProducts, ciscoPolicy=ciscoPolicy, ciscoPIB=ciscoPIB, ciscoPolicyAuto=ciscoPolicyAuto, ciscoPibToMib=ciscoPibToMib, ciscoDomains=ciscoDomains, ciscoTDomains=ciscoTDomains, ciscoTDomainUdpIpv4=ciscoTDomainUdpIpv4, ciscoTDomainUdpIpv6=ciscoTDomainUdpIpv6, ciscoTDomainTcpIpv4=ciscoTDomainTcpIpv4, ciscoTDomainTcpIpv6=ciscoTDomainTcpIpv6, ciscoTDomainLocal=ciscoTDomainLocal, ciscoTDomainClns=ciscoTDomainClns, ciscoTDomainCons=ciscoTDomainCons, ciscoTDomainDdp=ciscoTDomainDdp, ciscoTDomainIpx=ciscoTDomainIpx, ciscoTDomainSctpIpv4=ciscoTDomainSctpIpv4, ciscoTDomainSctpIpv6=ciscoTDomainSctpIpv6, ciscoCIB=ciscoCIB, ciscoCibMmiGroup=ciscoCibMmiGroup, ciscoCibProvGroup=ciscoCibProvGroup, ciscoPKI=ciscoPKI)

