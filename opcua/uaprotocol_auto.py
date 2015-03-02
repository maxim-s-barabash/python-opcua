'''
Autogenerate code from xml spec
'''

import struct

from .uatypes import *
from .object_ids import ObjectIds



class OpenFileMode(object):
    '''
    
    '''
    Read = 1
    Write = 2
    EraseExisiting = 4
    Append = 8

class IdType(object):
    '''
    The type of identifier used in a node id.
    '''
    Numeric = 0
    String = 1
    Guid = 2
    Opaque = 3

class NodeClass(object):
    '''
    A mask specifying the class of the node.
    '''
    Unspecified = 0
    Object = 1
    Variable = 2
    Method = 4
    ObjectType = 8
    VariableType = 16
    ReferenceType = 32
    DataType = 64
    View = 128

class ApplicationType(object):
    '''
    The types of applications.
    '''
    Server = 0
    Client = 1
    ClientAndServer = 2
    DiscoveryServer = 3

class MessageSecurityMode(object):
    '''
    The type of security to use on a message.
    '''
    Invalid = 0
    None_ = 1
    Sign = 2
    SignAndEncrypt = 3

class UserTokenType(object):
    '''
    The possible user token types.
    '''
    Anonymous = 0
    UserName = 1
    Certificate = 2
    IssuedToken = 3

class SecurityTokenRequestType(object):
    '''
    Indicates whether a token if being created or renewed.
    '''
    Issue = 0
    Renew = 1

class NodeAttributesMask(object):
    '''
    The bits used to specify default attributes for a new node.
    '''
    None_ = 0
    AccessLevel = 1
    ArrayDimensions = 2
    BrowseName = 4
    ContainsNoLoops = 8
    DataType = 16
    Description = 32
    DisplayName = 64
    EventNotifier = 128
    Executable = 256
    Historizing = 512
    InverseName = 1024
    IsAbstract = 2048
    MinimumSamplingInterval = 4096
    NodeClass = 8192
    NodeId = 16384
    Symmetric = 32768
    UserAccessLevel = 65536
    UserExecutable = 131072
    UserWriteMask = 262144
    ValueRank = 524288
    WriteMask = 1048576
    Value = 2097152
    All = 4194303
    BaseNode = 1335396
    Object = 1335524
    ObjectTypeOrDataType = 1337444
    Variable = 4026999
    VariableType = 3958902
    Method = 1466724
    ReferenceType = 1371236
    View = 1335532

class AttributeWriteMask(object):
    '''
    Define bits used to indicate which attributes are writeable.
    '''
    None_ = 0
    AccessLevel = 1
    ArrayDimensions = 2
    BrowseName = 4
    ContainsNoLoops = 8
    DataType = 16
    Description = 32
    DisplayName = 64
    EventNotifier = 128
    Executable = 256
    Historizing = 512
    InverseName = 1024
    IsAbstract = 2048
    MinimumSamplingInterval = 4096
    NodeClass = 8192
    NodeId = 16384
    Symmetric = 32768
    UserAccessLevel = 65536
    UserExecutable = 131072
    UserWriteMask = 262144
    ValueRank = 524288
    WriteMask = 1048576
    ValueForVariableType = 2097152

class BrowseDirection(object):
    '''
    The directions of the references to return.
    '''
    Forward = 0
    Inverse = 1
    Both = 2

class BrowseResultMask(object):
    '''
    A bit mask which specifies what should be returned in a browse response.
    '''
    None_ = 0
    ReferenceTypeId = 1
    IsForward = 2
    NodeClass = 4
    BrowseName = 8
    DisplayName = 16
    TypeDefinition = 32
    All = 63
    ReferenceTypeInfo = 3
    TargetInfo = 60

class ComplianceLevel(object):
    '''
    
    '''
    Untested = 0
    Partial = 1
    SelfTested = 2
    Certified = 3

class FilterOperator(object):
    '''
    
    '''
    Equals = 0
    IsNull = 1
    GreaterThan = 2
    LessThan = 3
    GreaterThanOrEqual = 4
    LessThanOrEqual = 5
    Like = 6
    Not = 7
    Between = 8
    InList = 9
    And = 10
    Or = 11
    Cast = 12
    InView = 13
    OfType = 14
    RelatedTo = 15
    BitwiseAnd = 16
    BitwiseOr = 17

class TimestampsToReturn(object):
    '''
    
    '''
    Source = 0
    Server = 1
    Both = 2
    Neither = 3

class HistoryUpdateType(object):
    '''
    
    '''
    Insert = 1
    Replace = 2
    Update = 3
    Delete = 4

class PerformUpdateType(object):
    '''
    
    '''
    Insert = 1
    Replace = 2
    Update = 3
    Remove = 4

class MonitoringMode(object):
    '''
    
    '''
    Disabled = 0
    Sampling = 1
    Reporting = 2

class DataChangeTrigger(object):
    '''
    
    '''
    Status = 0
    StatusValue = 1
    StatusValueTimestamp = 2

class DeadbandType(object):
    '''
    
    '''
    None_ = 0
    Absolute = 1
    Percent = 2

class EnumeratedTestType(object):
    '''
    A simple enumerated type used for testing.
    '''
    Red = 1
    Yellow = 4
    Green = 5

class RedundancySupport(object):
    '''
    
    '''
    None_ = 0
    Cold = 1
    Warm = 2
    Hot = 3
    Transparent = 4
    HotAndMirrored = 5

class ServerState(object):
    '''
    
    '''
    Running = 0
    Failed = 1
    NoConfiguration = 2
    Suspended = 3
    Shutdown = 4
    Test = 5
    CommunicationFault = 6
    Unknown = 7

class ModelChangeStructureVerbMask(object):
    '''
    
    '''
    NodeAdded = 1
    NodeDeleted = 2
    ReferenceAdded = 4
    ReferenceDeleted = 8
    DataTypeChanged = 16

class AxisScaleEnumeration(object):
    '''
    
    '''
    Linear = 0
    Log = 1
    Ln = 2

class ExceptionDeviationFormat(object):
    '''
    
    '''
    AbsoluteValue = 0
    PercentOfRange = 1
    PercentOfValue = 2
    PercentOfEURange = 3
    Unknown = 4

class ExtensionObject(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = NodeId()
        self.Encoding = 0
        self.Body = b''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Body: 
            packet.append(pack_uatype('ByteString', self.Body))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ExtensionObject()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Body = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'ExtensionObject(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class XmlElement(object):
    '''
    An XML element encoded as a UTF-8 string.
    '''
    def __init__(self):
        self.Length = 0
        self.Value = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Int32', self.Length))
        packet.append(struct.pack('<i', len(self.Value)))
        for fieldname in self.Value:
            packet.append(pack_uatype('Char', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = XmlElement()
        obj.Length = unpack_uatype('Int32', data)
        obj.Value = unpack_uatype_array('Char', data)
        return obj
    
    def __str__(self):
        return 'XmlElement(' + 'Length:' + str(self.Length) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class DiagnosticInfo(object):
    '''
    A recursive structure containing diagnostic information associated with a status code.
    '''
    def __init__(self):
        self.Encoding = 0
        self.SymbolicId = 0
        self.NamespaceURI = 0
        self.LocalizedText = 0
        self.AdditionalInfo = b''
        self.InnerStatusCode = StatusCode()
        self.InnerDiagnosticInfo = None
    
    def to_binary(self):
        if self.InnerDiagnosticInfo is None: self.InnerDiagnosticInfo = DiagnosticInfo()
        packet = []
        if self.SymbolicId: self.Encoding |= (1 << 0)
        if self.NamespaceURI: self.Encoding |= (1 << 1)
        if self.LocalizedText: self.Encoding |= (1 << 2)
        if self.AdditionalInfo: self.Encoding |= (1 << 4)
        if self.InnerStatusCode: self.Encoding |= (1 << 5)
        if self.InnerDiagnosticInfo: self.Encoding |= (1 << 6)
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.SymbolicId: 
            packet.append(pack_uatype('Int32', self.SymbolicId))
        if self.NamespaceURI: 
            packet.append(pack_uatype('Int32', self.NamespaceURI))
        if self.LocalizedText: 
            packet.append(pack_uatype('Int32', self.LocalizedText))
        if self.AdditionalInfo: 
            packet.append(pack_uatype('CharArray', self.AdditionalInfo))
        if self.InnerStatusCode: 
            packet.append(self.InnerStatusCode.to_binary())
        if self.InnerDiagnosticInfo: 
            packet.append(self.InnerDiagnosticInfo.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DiagnosticInfo()
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.SymbolicId = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 1):
            obj.NamespaceURI = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 2):
            obj.LocalizedText = unpack_uatype('Int32', data)
        if obj.Encoding & (1 << 4):
            obj.AdditionalInfo = unpack_uatype('CharArray', data)
        if obj.Encoding & (1 << 5):
            obj.InnerStatusCode = StatusCode.from_binary(data)
        if obj.Encoding & (1 << 6):
            obj.InnerDiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DiagnosticInfo(' + 'Encoding:' + str(self.Encoding) + ', '  + \
             'SymbolicId:' + str(self.SymbolicId) + ', '  + \
             'NamespaceURI:' + str(self.NamespaceURI) + ', '  + \
             'LocalizedText:' + str(self.LocalizedText) + ', '  + \
             'AdditionalInfo:' + str(self.AdditionalInfo) + ', '  + \
             'InnerStatusCode:' + str(self.InnerStatusCode) + ', '  + \
             'InnerDiagnosticInfo:' + str(self.InnerDiagnosticInfo) + ')'
    
    __repr__ = __str__
    
class LocalizedText(object):
    '''
    A string qualified with a namespace index.
    '''
    def __init__(self):
        self.Encoding = 0
        self.Locale = b''
        self.Text = b''
    
    def to_binary(self):
        packet = []
        if self.Locale: self.Encoding |= (1 << 0)
        if self.Text: self.Encoding |= (1 << 1)
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Locale: 
            packet.append(pack_uatype('CharArray', self.Locale))
        if self.Text: 
            packet.append(pack_uatype('CharArray', self.Text))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = LocalizedText()
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Locale = unpack_uatype('CharArray', data)
        if obj.Encoding & (1 << 1):
            obj.Text = unpack_uatype('CharArray', data)
        return obj
    
    def __str__(self):
        return 'LocalizedText(' + 'Encoding:' + str(self.Encoding) + ', '  + \
             'Locale:' + str(self.Locale) + ', '  + \
             'Text:' + str(self.Text) + ')'
    
    __repr__ = __str__
    
class Argument(object):
    '''
    An argument for a method.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.Argument_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Name = ''
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.Name))
        body.append(self.DataType.to_binary())
        body.append(pack_uatype('Int32', self.ValueRank))
        body.append(struct.pack('<i', len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            body.append(pack_uatype('UInt32', fieldname))
        body.append(self.Description.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Argument()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Name = unpack_uatype('String', data)
        obj.DataType = NodeId.from_binary(data)
        obj.ValueRank = unpack_uatype('Int32', data)
        obj.ArrayDimensions = unpack_uatype_array('UInt32', data)
        obj.Description = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'Argument(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Name:' + str(self.Name) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'Description:' + str(self.Description) + ')'
    
    __repr__ = __str__
    
class EnumValueType(object):
    '''
    A mapping between a value of an enumerated type and a name and description.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EnumValueType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Value = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Int64', self.Value))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EnumValueType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Value = unpack_uatype('Int64', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EnumValueType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ')'
    
    __repr__ = __str__
    
class TimeZoneDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TimeZoneDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Offset = 0
        self.DaylightSavingInOffset = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Int16', self.Offset))
        body.append(pack_uatype('Boolean', self.DaylightSavingInOffset))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TimeZoneDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Offset = unpack_uatype('Int16', data)
        obj.DaylightSavingInOffset = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'TimeZoneDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Offset:' + str(self.Offset) + ', '  + \
             'DaylightSavingInOffset:' + str(self.DaylightSavingInOffset) + ')'
    
    __repr__ = __str__
    
class ApplicationDescription(object):
    '''
    Describes an application and how to find it.
    '''
    def __init__(self):
        self.ApplicationUri = ''
        self.ProductUri = ''
        self.ApplicationName = LocalizedText()
        self.ApplicationType = 0
        self.GatewayServerUri = ''
        self.DiscoveryProfileUri = ''
        self.DiscoveryUrls = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.ApplicationUri))
        packet.append(pack_uatype('String', self.ProductUri))
        packet.append(self.ApplicationName.to_binary())
        packet.append(pack_uatype('UInt32', self.ApplicationType))
        packet.append(pack_uatype('String', self.GatewayServerUri))
        packet.append(pack_uatype('String', self.DiscoveryProfileUri))
        packet.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for fieldname in self.DiscoveryUrls:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ApplicationDescription()
        obj.ApplicationUri = unpack_uatype('String', data)
        obj.ProductUri = unpack_uatype('String', data)
        obj.ApplicationName = LocalizedText.from_binary(data)
        obj.ApplicationType = unpack_uatype('UInt32', data)
        obj.GatewayServerUri = unpack_uatype('String', data)
        obj.DiscoveryProfileUri = unpack_uatype('String', data)
        obj.DiscoveryUrls = unpack_uatype_array('String', data)
        return obj
    
    def __str__(self):
        return 'ApplicationDescription(' + 'ApplicationUri:' + str(self.ApplicationUri) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'ApplicationName:' + str(self.ApplicationName) + ', '  + \
             'ApplicationType:' + str(self.ApplicationType) + ', '  + \
             'GatewayServerUri:' + str(self.GatewayServerUri) + ', '  + \
             'DiscoveryProfileUri:' + str(self.DiscoveryProfileUri) + ', '  + \
             'DiscoveryUrls:' + str(self.DiscoveryUrls) + ')'
    
    __repr__ = __str__
    
class RequestHeader(object):
    '''
    The header passed with every server request.
    '''
    def __init__(self):
        self.AuthenticationToken = NodeId()
        self.Timestamp = DateTime()
        self.RequestHandle = 0
        self.ReturnDiagnostics = 0
        self.AuditEntryId = ''
        self.TimeoutHint = 0
        self.AdditionalHeader = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(self.Timestamp.to_binary())
        packet.append(pack_uatype('UInt32', self.RequestHandle))
        packet.append(pack_uatype('UInt32', self.ReturnDiagnostics))
        packet.append(pack_uatype('String', self.AuditEntryId))
        packet.append(pack_uatype('UInt32', self.TimeoutHint))
        packet.append(self.AdditionalHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RequestHeader()
        obj.AuthenticationToken = NodeId.from_binary(data)
        obj.Timestamp = DateTime.from_binary(data)
        obj.RequestHandle = unpack_uatype('UInt32', data)
        obj.ReturnDiagnostics = unpack_uatype('UInt32', data)
        obj.AuditEntryId = unpack_uatype('String', data)
        obj.TimeoutHint = unpack_uatype('UInt32', data)
        obj.AdditionalHeader = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RequestHeader(' + 'AuthenticationToken:' + str(self.AuthenticationToken) + ', '  + \
             'Timestamp:' + str(self.Timestamp) + ', '  + \
             'RequestHandle:' + str(self.RequestHandle) + ', '  + \
             'ReturnDiagnostics:' + str(self.ReturnDiagnostics) + ', '  + \
             'AuditEntryId:' + str(self.AuditEntryId) + ', '  + \
             'TimeoutHint:' + str(self.TimeoutHint) + ', '  + \
             'AdditionalHeader:' + str(self.AdditionalHeader) + ')'
    
    __repr__ = __str__
    
class ResponseHeader(object):
    '''
    The header passed with every server response.
    '''
    def __init__(self):
        self.Timestamp = DateTime()
        self.RequestHandle = 0
        self.ServiceResult = StatusCode()
        self.ServiceDiagnostics = DiagnosticInfo()
        self.StringTable = []
        self.AdditionalHeader = ExtensionObject()
    
    def to_binary(self):
        packet = []
        packet.append(self.Timestamp.to_binary())
        packet.append(pack_uatype('UInt32', self.RequestHandle))
        packet.append(self.ServiceResult.to_binary())
        packet.append(self.ServiceDiagnostics.to_binary())
        packet.append(struct.pack('<i', len(self.StringTable)))
        for fieldname in self.StringTable:
            packet.append(pack_uatype('String', fieldname))
        packet.append(self.AdditionalHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ResponseHeader()
        obj.Timestamp = DateTime.from_binary(data)
        obj.RequestHandle = unpack_uatype('UInt32', data)
        obj.ServiceResult = StatusCode.from_binary(data)
        obj.ServiceDiagnostics = DiagnosticInfo.from_binary(data)
        obj.StringTable = unpack_uatype_array('String', data)
        obj.AdditionalHeader = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ResponseHeader(' + 'Timestamp:' + str(self.Timestamp) + ', '  + \
             'RequestHandle:' + str(self.RequestHandle) + ', '  + \
             'ServiceResult:' + str(self.ServiceResult) + ', '  + \
             'ServiceDiagnostics:' + str(self.ServiceDiagnostics) + ', '  + \
             'StringTable:' + str(self.StringTable) + ', '  + \
             'AdditionalHeader:' + str(self.AdditionalHeader) + ')'
    
    __repr__ = __str__
    
class ServiceFault(object):
    '''
    The response returned by all services when there is a service level error.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ServiceFault_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.ResponseHeader.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServiceFault()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ServiceFault(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class FindServersParameters(object):
    '''
    
    '''
    def __init__(self):
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ServerUris = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(struct.pack('<i', len(self.ServerUris)))
        for fieldname in self.ServerUris:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersParameters()
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.ServerUris = unpack_uatype_array('String', data)
        return obj
    
    def __str__(self):
        return 'FindServersParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'ServerUris:' + str(self.ServerUris) + ')'
    
    __repr__ = __str__
    
class FindServersRequest(object):
    '''
    Finds the servers known to the discovery server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = FindServersParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = FindServersParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'FindServersRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class FindServersResult(object):
    '''
    
    '''
    def __init__(self):
        self.Servers = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Servers)))
        for fieldname in self.Servers:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Servers.append(ApplicationDescription.from_binary(data))
        return obj
    
    def __str__(self):
        return 'FindServersResult(' + 'Servers:' + str(self.Servers) + ')'
    
    __repr__ = __str__
    
class FindServersResponse(object):
    '''
    Finds the servers known to the discovery server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.FindServersResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = FindServersResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = FindServersResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = FindServersResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'FindServersResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UserTokenPolicy(object):
    '''
    Describes a user token that can be used with a server.
    '''
    def __init__(self):
        self.PolicyId = ''
        self.TokenType = 0
        self.IssuedTokenType = ''
        self.IssuerEndpointUrl = ''
        self.SecurityPolicyUri = ''
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.PolicyId))
        packet.append(pack_uatype('UInt32', self.TokenType))
        packet.append(pack_uatype('String', self.IssuedTokenType))
        packet.append(pack_uatype('String', self.IssuerEndpointUrl))
        packet.append(pack_uatype('String', self.SecurityPolicyUri))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UserTokenPolicy()
        obj.PolicyId = unpack_uatype('String', data)
        obj.TokenType = unpack_uatype('UInt32', data)
        obj.IssuedTokenType = unpack_uatype('String', data)
        obj.IssuerEndpointUrl = unpack_uatype('String', data)
        obj.SecurityPolicyUri = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'UserTokenPolicy(' + 'PolicyId:' + str(self.PolicyId) + ', '  + \
             'TokenType:' + str(self.TokenType) + ', '  + \
             'IssuedTokenType:' + str(self.IssuedTokenType) + ', '  + \
             'IssuerEndpointUrl:' + str(self.IssuerEndpointUrl) + ', '  + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ')'
    
    __repr__ = __str__
    
class EndpointDescription(object):
    '''
    The description of a endpoint that can be used to access a server.
    '''
    def __init__(self):
        self.EndpointUrl = ''
        self.Server = ApplicationDescription()
        self.ServerCertificate = b''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.UserIdentityTokens = []
        self.TransportProfileUri = ''
        self.SecurityLevel = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(self.Server.to_binary())
        packet.append(pack_uatype('ByteString', self.ServerCertificate))
        packet.append(pack_uatype('UInt32', self.SecurityMode))
        packet.append(pack_uatype('String', self.SecurityPolicyUri))
        packet.append(struct.pack('<i', len(self.UserIdentityTokens)))
        for fieldname in self.UserIdentityTokens:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('String', self.TransportProfileUri))
        packet.append(pack_uatype('Byte', self.SecurityLevel))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EndpointDescription()
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.Server = ApplicationDescription.from_binary(data)
        obj.ServerCertificate = unpack_uatype('ByteString', data)
        obj.SecurityMode = unpack_uatype('UInt32', data)
        obj.SecurityPolicyUri = unpack_uatype('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.UserIdentityTokens.append(UserTokenPolicy.from_binary(data))
        obj.TransportProfileUri = unpack_uatype('String', data)
        obj.SecurityLevel = unpack_uatype('Byte', data)
        return obj
    
    def __str__(self):
        return 'EndpointDescription(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'Server:' + str(self.Server) + ', '  + \
             'ServerCertificate:' + str(self.ServerCertificate) + ', '  + \
             'SecurityMode:' + str(self.SecurityMode) + ', '  + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', '  + \
             'UserIdentityTokens:' + str(self.UserIdentityTokens) + ', '  + \
             'TransportProfileUri:' + str(self.TransportProfileUri) + ', '  + \
             'SecurityLevel:' + str(self.SecurityLevel) + ')'
    
    __repr__ = __str__
    
class GetEndpointsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ProfileUris = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(struct.pack('<i', len(self.ProfileUris)))
        for fieldname in self.ProfileUris:
            packet.append(pack_uatype('String', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = GetEndpointsParameters()
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.ProfileUris = unpack_uatype_array('String', data)
        return obj
    
    def __str__(self):
        return 'GetEndpointsParameters(' + 'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'ProfileUris:' + str(self.ProfileUris) + ')'
    
    __repr__ = __str__
    
class GetEndpointsRequest(object):
    '''
    Gets the endpoints used by the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = GetEndpointsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = GetEndpointsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = GetEndpointsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'GetEndpointsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class GetEndpointsResponse(object):
    '''
    Gets the endpoints used by the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.GetEndpointsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Endpoints = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Endpoints)))
        for fieldname in self.Endpoints:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = GetEndpointsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Endpoints.append(EndpointDescription.from_binary(data))
        return obj
    
    def __str__(self):
        return 'GetEndpointsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Endpoints:' + str(self.Endpoints) + ')'
    
    __repr__ = __str__
    
class RegisteredServer(object):
    '''
    The information required to register a server with a discovery server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisteredServer_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ServerUri = ''
        self.ProductUri = ''
        self.ServerNames = []
        self.ServerType = 0
        self.GatewayServerUri = ''
        self.DiscoveryUrls = []
        self.SemaphoreFilePath = ''
        self.IsOnline = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.ServerUri))
        body.append(pack_uatype('String', self.ProductUri))
        body.append(struct.pack('<i', len(self.ServerNames)))
        for fieldname in self.ServerNames:
            body.append(fieldname.to_binary())
        body.append(pack_uatype('UInt32', self.ServerType))
        body.append(pack_uatype('String', self.GatewayServerUri))
        body.append(struct.pack('<i', len(self.DiscoveryUrls)))
        for fieldname in self.DiscoveryUrls:
            body.append(pack_uatype('String', fieldname))
        body.append(pack_uatype('String', self.SemaphoreFilePath))
        body.append(pack_uatype('Boolean', self.IsOnline))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisteredServer()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ServerUri = unpack_uatype('String', data)
        obj.ProductUri = unpack_uatype('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ServerNames.append(LocalizedText.from_binary(data))
        obj.ServerType = unpack_uatype('UInt32', data)
        obj.GatewayServerUri = unpack_uatype('String', data)
        obj.DiscoveryUrls = unpack_uatype_array('String', data)
        obj.SemaphoreFilePath = unpack_uatype('String', data)
        obj.IsOnline = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'RegisteredServer(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ServerUri:' + str(self.ServerUri) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'ServerNames:' + str(self.ServerNames) + ', '  + \
             'ServerType:' + str(self.ServerType) + ', '  + \
             'GatewayServerUri:' + str(self.GatewayServerUri) + ', '  + \
             'DiscoveryUrls:' + str(self.DiscoveryUrls) + ', '  + \
             'SemaphoreFilePath:' + str(self.SemaphoreFilePath) + ', '  + \
             'IsOnline:' + str(self.IsOnline) + ')'
    
    __repr__ = __str__
    
class RegisterServerParameters(object):
    '''
    
    '''
    def __init__(self):
        self.Server = RegisteredServer()
    
    def to_binary(self):
        packet = []
        packet.append(self.Server.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterServerParameters()
        obj.Server = RegisteredServer.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterServerParameters(' + 'Server:' + str(self.Server) + ')'
    
    __repr__ = __str__
    
class RegisterServerRequest(object):
    '''
    Registers a server with the discovery server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterServerParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterServerRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RegisterServerParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterServerRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RegisterServerResponse(object):
    '''
    Registers a server with the discovery server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterServerResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterServerResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterServerResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class ChannelSecurityToken(object):
    '''
    The token that identifies a set of keys for an active secure channel.
    '''
    def __init__(self):
        self.ChannelId = 0
        self.TokenId = 0
        self.CreatedAt = DateTime()
        self.RevisedLifetime = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ChannelId))
        packet.append(pack_uatype('UInt32', self.TokenId))
        packet.append(self.CreatedAt.to_binary())
        packet.append(pack_uatype('UInt32', self.RevisedLifetime))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ChannelSecurityToken()
        obj.ChannelId = unpack_uatype('UInt32', data)
        obj.TokenId = unpack_uatype('UInt32', data)
        obj.CreatedAt = DateTime.from_binary(data)
        obj.RevisedLifetime = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ChannelSecurityToken(' + 'ChannelId:' + str(self.ChannelId) + ', '  + \
             'TokenId:' + str(self.TokenId) + ', '  + \
             'CreatedAt:' + str(self.CreatedAt) + ', '  + \
             'RevisedLifetime:' + str(self.RevisedLifetime) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ClientProtocolVersion = 0
        self.RequestType = 0
        self.SecurityMode = 0
        self.ClientNonce = b''
        self.RequestedLifetime = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ClientProtocolVersion))
        packet.append(pack_uatype('UInt32', self.RequestType))
        packet.append(pack_uatype('UInt32', self.SecurityMode))
        packet.append(pack_uatype('ByteString', self.ClientNonce))
        packet.append(pack_uatype('UInt32', self.RequestedLifetime))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelParameters()
        obj.ClientProtocolVersion = unpack_uatype('UInt32', data)
        obj.RequestType = unpack_uatype('UInt32', data)
        obj.SecurityMode = unpack_uatype('UInt32', data)
        obj.ClientNonce = unpack_uatype('ByteString', data)
        obj.RequestedLifetime = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelParameters(' + 'ClientProtocolVersion:' + str(self.ClientProtocolVersion) + ', '  + \
             'RequestType:' + str(self.RequestType) + ', '  + \
             'SecurityMode:' + str(self.SecurityMode) + ', '  + \
             'ClientNonce:' + str(self.ClientNonce) + ', '  + \
             'RequestedLifetime:' + str(self.RequestedLifetime) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelRequest(object):
    '''
    Creates a secure channel with a server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = OpenSecureChannelParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = OpenSecureChannelParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelResult(object):
    '''
    
    '''
    def __init__(self):
        self.ServerProtocolVersion = 0
        self.SecurityToken = ChannelSecurityToken()
        self.ServerNonce = b''
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.ServerProtocolVersion))
        packet.append(self.SecurityToken.to_binary())
        packet.append(pack_uatype('ByteString', self.ServerNonce))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelResult()
        obj.ServerProtocolVersion = unpack_uatype('UInt32', data)
        obj.SecurityToken = ChannelSecurityToken.from_binary(data)
        obj.ServerNonce = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelResult(' + 'ServerProtocolVersion:' + str(self.ServerProtocolVersion) + ', '  + \
             'SecurityToken:' + str(self.SecurityToken) + ', '  + \
             'ServerNonce:' + str(self.ServerNonce) + ')'
    
    __repr__ = __str__
    
class OpenSecureChannelResponse(object):
    '''
    Creates a secure channel with a server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.OpenSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = OpenSecureChannelResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = OpenSecureChannelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = OpenSecureChannelResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'OpenSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CloseSecureChannelRequest(object):
    '''
    Closes a secure channel.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CloseSecureChannelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CloseSecureChannelRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ')'
    
    __repr__ = __str__
    
class CloseSecureChannelResponse(object):
    '''
    Closes a secure channel.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSecureChannelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CloseSecureChannelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CloseSecureChannelResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class SignedSoftwareCertificate(object):
    '''
    A software certificate with a digital signature.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SignedSoftwareCertificate_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.CertificateData = b''
        self.Signature = b''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('ByteString', self.CertificateData))
        body.append(pack_uatype('ByteString', self.Signature))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SignedSoftwareCertificate()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.CertificateData = unpack_uatype('ByteString', data)
        obj.Signature = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'SignedSoftwareCertificate(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'CertificateData:' + str(self.CertificateData) + ', '  + \
             'Signature:' + str(self.Signature) + ')'
    
    __repr__ = __str__
    
class SignatureData(object):
    '''
    A digital signature.
    '''
    def __init__(self):
        self.Algorithm = ''
        self.Signature = b''
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('String', self.Algorithm))
        packet.append(pack_uatype('ByteString', self.Signature))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SignatureData()
        obj.Algorithm = unpack_uatype('String', data)
        obj.Signature = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'SignatureData(' + 'Algorithm:' + str(self.Algorithm) + ', '  + \
             'Signature:' + str(self.Signature) + ')'
    
    __repr__ = __str__
    
class CreateSessionParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.SessionName = ''
        self.ClientNonce = b''
        self.ClientCertificate = b''
        self.RequestedSessionTimeout = 0
        self.MaxResponseMessageSize = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.ClientDescription.to_binary())
        packet.append(pack_uatype('String', self.ServerUri))
        packet.append(pack_uatype('String', self.EndpointUrl))
        packet.append(pack_uatype('String', self.SessionName))
        packet.append(pack_uatype('ByteString', self.ClientNonce))
        packet.append(pack_uatype('ByteString', self.ClientCertificate))
        packet.append(pack_uatype('Double', self.RequestedSessionTimeout))
        packet.append(pack_uatype('UInt32', self.MaxResponseMessageSize))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSessionParameters()
        obj.ClientDescription = ApplicationDescription.from_binary(data)
        obj.ServerUri = unpack_uatype('String', data)
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.SessionName = unpack_uatype('String', data)
        obj.ClientNonce = unpack_uatype('ByteString', data)
        obj.ClientCertificate = unpack_uatype('ByteString', data)
        obj.RequestedSessionTimeout = unpack_uatype('Double', data)
        obj.MaxResponseMessageSize = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'CreateSessionParameters(' + 'ClientDescription:' + str(self.ClientDescription) + ', '  + \
             'ServerUri:' + str(self.ServerUri) + ', '  + \
             'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'SessionName:' + str(self.SessionName) + ', '  + \
             'ClientNonce:' + str(self.ClientNonce) + ', '  + \
             'ClientCertificate:' + str(self.ClientCertificate) + ', '  + \
             'RequestedSessionTimeout:' + str(self.RequestedSessionTimeout) + ', '  + \
             'MaxResponseMessageSize:' + str(self.MaxResponseMessageSize) + ')'
    
    __repr__ = __str__
    
class CreateSessionRequest(object):
    '''
    Creates a new session with the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSessionParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateSessionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateSessionResult(object):
    '''
    
    '''
    def __init__(self):
        self.SessionId = NodeId()
        self.AuthenticationToken = NodeId()
        self.RevisedSessionTimeout = 0
        self.ServerNonce = b''
        self.ServerCertificate = b''
        self.ServerEndpoints = []
        self.ServerSoftwareCertificates = []
        self.ServerSignature = SignatureData()
        self.MaxRequestMessageSize = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.SessionId.to_binary())
        packet.append(self.AuthenticationToken.to_binary())
        packet.append(pack_uatype('Double', self.RevisedSessionTimeout))
        packet.append(pack_uatype('ByteString', self.ServerNonce))
        packet.append(pack_uatype('ByteString', self.ServerCertificate))
        packet.append(struct.pack('<i', len(self.ServerEndpoints)))
        for fieldname in self.ServerEndpoints:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.ServerSoftwareCertificates)))
        for fieldname in self.ServerSoftwareCertificates:
            packet.append(fieldname.to_binary())
        packet.append(self.ServerSignature.to_binary())
        packet.append(pack_uatype('UInt32', self.MaxRequestMessageSize))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSessionResult()
        obj.SessionId = NodeId.from_binary(data)
        obj.AuthenticationToken = NodeId.from_binary(data)
        obj.RevisedSessionTimeout = unpack_uatype('Double', data)
        obj.ServerNonce = unpack_uatype('ByteString', data)
        obj.ServerCertificate = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ServerEndpoints.append(EndpointDescription.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ServerSoftwareCertificates.append(SignedSoftwareCertificate.from_binary(data))
        obj.ServerSignature = SignatureData.from_binary(data)
        obj.MaxRequestMessageSize = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'CreateSessionResult(' + 'SessionId:' + str(self.SessionId) + ', '  + \
             'AuthenticationToken:' + str(self.AuthenticationToken) + ', '  + \
             'RevisedSessionTimeout:' + str(self.RevisedSessionTimeout) + ', '  + \
             'ServerNonce:' + str(self.ServerNonce) + ', '  + \
             'ServerCertificate:' + str(self.ServerCertificate) + ', '  + \
             'ServerEndpoints:' + str(self.ServerEndpoints) + ', '  + \
             'ServerSoftwareCertificates:' + str(self.ServerSoftwareCertificates) + ', '  + \
             'ServerSignature:' + str(self.ServerSignature) + ', '  + \
             'MaxRequestMessageSize:' + str(self.MaxRequestMessageSize) + ')'
    
    __repr__ = __str__
    
class CreateSessionResponse(object):
    '''
    Creates a new session with the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSessionResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateSessionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UserIdentityToken(object):
    '''
    A base type for a user identity token.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UserIdentityToken_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.PolicyId = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.PolicyId))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UserIdentityToken()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.PolicyId = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'UserIdentityToken(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'PolicyId:' + str(self.PolicyId) + ')'
    
    __repr__ = __str__
    
class AnonymousIdentityToken(object):
    '''
    A token representing an anonymous user.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AnonymousIdentityToken_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.PolicyId = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.PolicyId))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AnonymousIdentityToken()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.PolicyId = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'AnonymousIdentityToken(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'PolicyId:' + str(self.PolicyId) + ')'
    
    __repr__ = __str__
    
class UserNameIdentityToken(object):
    '''
    A token representing a user identified by a user name and password.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UserNameIdentityToken_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.PolicyId = ''
        self.UserName = ''
        self.Password = b''
        self.EncryptionAlgorithm = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.PolicyId))
        body.append(pack_uatype('String', self.UserName))
        body.append(pack_uatype('ByteString', self.Password))
        body.append(pack_uatype('String', self.EncryptionAlgorithm))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UserNameIdentityToken()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.PolicyId = unpack_uatype('String', data)
        obj.UserName = unpack_uatype('String', data)
        obj.Password = unpack_uatype('ByteString', data)
        obj.EncryptionAlgorithm = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'UserNameIdentityToken(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'PolicyId:' + str(self.PolicyId) + ', '  + \
             'UserName:' + str(self.UserName) + ', '  + \
             'Password:' + str(self.Password) + ', '  + \
             'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'
    
    __repr__ = __str__
    
class X509IdentityToken(object):
    '''
    A token representing a user identified by an X509 certificate.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.X509IdentityToken_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.PolicyId = ''
        self.CertificateData = b''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.PolicyId))
        body.append(pack_uatype('ByteString', self.CertificateData))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = X509IdentityToken()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.PolicyId = unpack_uatype('String', data)
        obj.CertificateData = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'X509IdentityToken(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'PolicyId:' + str(self.PolicyId) + ', '  + \
             'CertificateData:' + str(self.CertificateData) + ')'
    
    __repr__ = __str__
    
class IssuedIdentityToken(object):
    '''
    A token representing a user identified by a WS-Security XML token.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.IssuedIdentityToken_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.PolicyId = ''
        self.TokenData = b''
        self.EncryptionAlgorithm = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.PolicyId))
        body.append(pack_uatype('ByteString', self.TokenData))
        body.append(pack_uatype('String', self.EncryptionAlgorithm))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = IssuedIdentityToken()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.PolicyId = unpack_uatype('String', data)
        obj.TokenData = unpack_uatype('ByteString', data)
        obj.EncryptionAlgorithm = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'IssuedIdentityToken(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'PolicyId:' + str(self.PolicyId) + ', '  + \
             'TokenData:' + str(self.TokenData) + ', '  + \
             'EncryptionAlgorithm:' + str(self.EncryptionAlgorithm) + ')'
    
    __repr__ = __str__
    
class ActivateSessionParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ClientSignature = SignatureData()
        self.ClientSoftwareCertificates = []
        self.LocaleIds = []
        self.UserIdentityToken = ExtensionObject()
        self.UserTokenSignature = SignatureData()
    
    def to_binary(self):
        packet = []
        packet.append(self.ClientSignature.to_binary())
        packet.append(struct.pack('<i', len(self.ClientSoftwareCertificates)))
        for fieldname in self.ClientSoftwareCertificates:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            packet.append(pack_uatype('String', fieldname))
        packet.append(self.UserIdentityToken.to_binary())
        packet.append(self.UserTokenSignature.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ActivateSessionParameters()
        obj.ClientSignature = SignatureData.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ClientSoftwareCertificates.append(SignedSoftwareCertificate.from_binary(data))
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.UserIdentityToken = ExtensionObject.from_binary(data)
        obj.UserTokenSignature = SignatureData.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionParameters(' + 'ClientSignature:' + str(self.ClientSignature) + ', '  + \
             'ClientSoftwareCertificates:' + str(self.ClientSoftwareCertificates) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'UserIdentityToken:' + str(self.UserIdentityToken) + ', '  + \
             'UserTokenSignature:' + str(self.UserTokenSignature) + ')'
    
    __repr__ = __str__
    
class ActivateSessionRequest(object):
    '''
    Activates a session with the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ActivateSessionParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ActivateSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ActivateSessionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ActivateSessionResult(object):
    '''
    
    '''
    def __init__(self):
        self.ServerNonce = b''
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('ByteString', self.ServerNonce))
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ActivateSessionResult()
        obj.ServerNonce = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ActivateSessionResult(' + 'ServerNonce:' + str(self.ServerNonce) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ActivateSessionResponse(object):
    '''
    Activates a session with the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ActivateSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ActivateSessionResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ActivateSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ActivateSessionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ActivateSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CloseSessionRequest(object):
    '''
    Closes a session with the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.DeleteSubscriptions = True
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(pack_uatype('Boolean', self.DeleteSubscriptions))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CloseSessionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.DeleteSubscriptions = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'CloseSessionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'DeleteSubscriptions:' + str(self.DeleteSubscriptions) + ')'
    
    __repr__ = __str__
    
class CloseSessionResponse(object):
    '''
    Closes a session with the server.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CloseSessionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CloseSessionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CloseSessionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class CancelParameters(object):
    '''
    
    '''
    def __init__(self):
        self.RequestHandle = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.RequestHandle))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CancelParameters()
        obj.RequestHandle = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'CancelParameters(' + 'RequestHandle:' + str(self.RequestHandle) + ')'
    
    __repr__ = __str__
    
class CancelRequest(object):
    '''
    Cancels an outstanding request.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CancelRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CancelParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CancelRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CancelParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CancelRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CancelResult(object):
    '''
    
    '''
    def __init__(self):
        self.CancelCount = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.CancelCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CancelResult()
        obj.CancelCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'CancelResult(' + 'CancelCount:' + str(self.CancelCount) + ')'
    
    __repr__ = __str__
    
class CancelResponse(object):
    '''
    Cancels an outstanding request.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CancelResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CancelResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CancelResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CancelResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CancelResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class NodeAttributes(object):
    '''
    The base attributes for all nodes.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.NodeAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NodeAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'NodeAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ')'
    
    __repr__ = __str__
    
class ObjectAttributes(object):
    '''
    The attributes for an object node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ObjectAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.EventNotifier = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(pack_uatype('Byte', self.EventNotifier))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ObjectAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.EventNotifier = unpack_uatype('Byte', data)
        return obj
    
    def __str__(self):
        return 'ObjectAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'EventNotifier:' + str(self.EventNotifier) + ')'
    
    __repr__ = __str__
    
class VariableAttributes(object):
    '''
    The attributes for a variable node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.VariableAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.AccessLevel = 0
        self.UserAccessLevel = 0
        self.MinimumSamplingInterval = 0
        self.Historizing = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(self.Value.to_binary())
        body.append(self.DataType.to_binary())
        body.append(pack_uatype('Int32', self.ValueRank))
        body.append(struct.pack('<i', len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            body.append(pack_uatype('UInt32', fieldname))
        body.append(pack_uatype('Byte', self.AccessLevel))
        body.append(pack_uatype('Byte', self.UserAccessLevel))
        body.append(pack_uatype('Double', self.MinimumSamplingInterval))
        body.append(pack_uatype('Boolean', self.Historizing))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = VariableAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        obj.ValueRank = unpack_uatype('Int32', data)
        obj.ArrayDimensions = unpack_uatype_array('UInt32', data)
        obj.AccessLevel = unpack_uatype('Byte', data)
        obj.UserAccessLevel = unpack_uatype('Byte', data)
        obj.MinimumSamplingInterval = unpack_uatype('Double', data)
        obj.Historizing = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'VariableAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'AccessLevel:' + str(self.AccessLevel) + ', '  + \
             'UserAccessLevel:' + str(self.UserAccessLevel) + ', '  + \
             'MinimumSamplingInterval:' + str(self.MinimumSamplingInterval) + ', '  + \
             'Historizing:' + str(self.Historizing) + ')'
    
    __repr__ = __str__
    
class MethodAttributes(object):
    '''
    The attributes for a method node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MethodAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Executable = True
        self.UserExecutable = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(pack_uatype('Boolean', self.Executable))
        body.append(pack_uatype('Boolean', self.UserExecutable))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MethodAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.Executable = unpack_uatype('Boolean', data)
        obj.UserExecutable = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'MethodAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'Executable:' + str(self.Executable) + ', '  + \
             'UserExecutable:' + str(self.UserExecutable) + ')'
    
    __repr__ = __str__
    
class ObjectTypeAttributes(object):
    '''
    The attributes for an object type node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ObjectTypeAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(pack_uatype('Boolean', self.IsAbstract))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ObjectTypeAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'ObjectTypeAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class VariableTypeAttributes(object):
    '''
    The attributes for a variable type node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.VariableTypeAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.Value = Variant()
        self.DataType = NodeId()
        self.ValueRank = 0
        self.ArrayDimensions = []
        self.IsAbstract = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(self.Value.to_binary())
        body.append(self.DataType.to_binary())
        body.append(pack_uatype('Int32', self.ValueRank))
        body.append(struct.pack('<i', len(self.ArrayDimensions)))
        for fieldname in self.ArrayDimensions:
            body.append(pack_uatype('UInt32', fieldname))
        body.append(pack_uatype('Boolean', self.IsAbstract))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = VariableTypeAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.Value = Variant.from_binary(data)
        obj.DataType = NodeId.from_binary(data)
        obj.ValueRank = unpack_uatype('Int32', data)
        obj.ArrayDimensions = unpack_uatype_array('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'VariableTypeAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'Value:' + str(self.Value) + ', '  + \
             'DataType:' + str(self.DataType) + ', '  + \
             'ValueRank:' + str(self.ValueRank) + ', '  + \
             'ArrayDimensions:' + str(self.ArrayDimensions) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class ReferenceTypeAttributes(object):
    '''
    The attributes for a reference type node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReferenceTypeAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
        self.Symmetric = True
        self.InverseName = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(pack_uatype('Boolean', self.IsAbstract))
        body.append(pack_uatype('Boolean', self.Symmetric))
        body.append(self.InverseName.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReferenceTypeAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        obj.Symmetric = unpack_uatype('Boolean', data)
        obj.InverseName = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReferenceTypeAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ', '  + \
             'Symmetric:' + str(self.Symmetric) + ', '  + \
             'InverseName:' + str(self.InverseName) + ')'
    
    __repr__ = __str__
    
class DataTypeAttributes(object):
    '''
    The attributes for a data type node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DataTypeAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.IsAbstract = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(pack_uatype('Boolean', self.IsAbstract))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataTypeAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.IsAbstract = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'DataTypeAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'IsAbstract:' + str(self.IsAbstract) + ')'
    
    __repr__ = __str__
    
class ViewAttributes(object):
    '''
    The attributes for a view node.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ViewAttributes_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SpecifiedAttributes = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
        self.WriteMask = 0
        self.UserWriteMask = 0
        self.ContainsNoLoops = True
        self.EventNotifier = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SpecifiedAttributes))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body.append(pack_uatype('UInt32', self.WriteMask))
        body.append(pack_uatype('UInt32', self.UserWriteMask))
        body.append(pack_uatype('Boolean', self.ContainsNoLoops))
        body.append(pack_uatype('Byte', self.EventNotifier))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ViewAttributes()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SpecifiedAttributes = unpack_uatype('UInt32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        obj.WriteMask = unpack_uatype('UInt32', data)
        obj.UserWriteMask = unpack_uatype('UInt32', data)
        obj.ContainsNoLoops = unpack_uatype('Boolean', data)
        obj.EventNotifier = unpack_uatype('Byte', data)
        return obj
    
    def __str__(self):
        return 'ViewAttributes(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SpecifiedAttributes:' + str(self.SpecifiedAttributes) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ', '  + \
             'WriteMask:' + str(self.WriteMask) + ', '  + \
             'UserWriteMask:' + str(self.UserWriteMask) + ', '  + \
             'ContainsNoLoops:' + str(self.ContainsNoLoops) + ', '  + \
             'EventNotifier:' + str(self.EventNotifier) + ')'
    
    __repr__ = __str__
    
class AddNodesItem(object):
    '''
    A request to add a node to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesItem_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ParentNodeId = ExpandedNodeId()
        self.ReferenceTypeId = NodeId()
        self.RequestedNewNodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.NodeClass = 0
        self.NodeAttributes = ExtensionObject()
        self.TypeDefinition = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.ParentNodeId.to_binary())
        body.append(self.ReferenceTypeId.to_binary())
        body.append(self.RequestedNewNodeId.to_binary())
        body.append(self.BrowseName.to_binary())
        body.append(pack_uatype('UInt32', self.NodeClass))
        body.append(self.NodeAttributes.to_binary())
        body.append(self.TypeDefinition.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesItem()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ParentNodeId = ExpandedNodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.RequestedNewNodeId = ExpandedNodeId.from_binary(data)
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.NodeClass = unpack_uatype('UInt32', data)
        obj.NodeAttributes = ExtensionObject.from_binary(data)
        obj.TypeDefinition = ExpandedNodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesItem(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ParentNodeId:' + str(self.ParentNodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'RequestedNewNodeId:' + str(self.RequestedNewNodeId) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'NodeAttributes:' + str(self.NodeAttributes) + ', '  + \
             'TypeDefinition:' + str(self.TypeDefinition) + ')'
    
    __repr__ = __str__
    
class AddNodesResult(object):
    '''
    A result of an add node operation.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.AddedNodeId = NodeId()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(self.AddedNodeId.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.AddedNodeId = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'AddedNodeId:' + str(self.AddedNodeId) + ')'
    
    __repr__ = __str__
    
class AddNodesParameters(object):
    '''
    
    '''
    def __init__(self):
        self.NodesToAdd = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToAdd)))
        for fieldname in self.NodesToAdd:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToAdd.append(AddNodesItem.from_binary(data))
        return obj
    
    def __str__(self):
        return 'AddNodesParameters(' + 'NodesToAdd:' + str(self.NodesToAdd) + ')'
    
    __repr__ = __str__
    
class AddNodesRequest(object):
    '''
    Adds one or more nodes to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddNodesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = AddNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class AddNodesResponse(object):
    '''
    Adds one or more nodes to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(AddNodesResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'AddNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class AddReferencesItem(object):
    '''
    A request to add a reference to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesItem_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetServerUri = ''
        self.TargetNodeId = ExpandedNodeId()
        self.TargetNodeClass = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.SourceNodeId.to_binary())
        body.append(self.ReferenceTypeId.to_binary())
        body.append(pack_uatype('Boolean', self.IsForward))
        body.append(pack_uatype('String', self.TargetServerUri))
        body.append(self.TargetNodeId.to_binary())
        body.append(pack_uatype('UInt32', self.TargetNodeClass))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesItem()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SourceNodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        obj.TargetServerUri = unpack_uatype('String', data)
        obj.TargetNodeId = ExpandedNodeId.from_binary(data)
        obj.TargetNodeClass = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'AddReferencesItem(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SourceNodeId:' + str(self.SourceNodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'TargetServerUri:' + str(self.TargetServerUri) + ', '  + \
             'TargetNodeId:' + str(self.TargetNodeId) + ', '  + \
             'TargetNodeClass:' + str(self.TargetNodeClass) + ')'
    
    __repr__ = __str__
    
class AddReferencesParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ReferencesToAdd = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ReferencesToAdd)))
        for fieldname in self.ReferencesToAdd:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ReferencesToAdd.append(AddReferencesItem.from_binary(data))
        return obj
    
    def __str__(self):
        return 'AddReferencesParameters(' + 'ReferencesToAdd:' + str(self.ReferencesToAdd) + ')'
    
    __repr__ = __str__
    
class AddReferencesRequest(object):
    '''
    Adds one or more references to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = AddReferencesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = AddReferencesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class AddReferencesResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'AddReferencesResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class AddReferencesResponse(object):
    '''
    Adds one or more references to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AddReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = AddReferencesResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AddReferencesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = AddReferencesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AddReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteNodesItem(object):
    '''
    A request to delete a node to the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesItem_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.DeleteTargetReferences = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('Boolean', self.DeleteTargetReferences))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesItem()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.DeleteTargetReferences = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesItem(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'DeleteTargetReferences:' + str(self.DeleteTargetReferences) + ')'
    
    __repr__ = __str__
    
class DeleteNodesParameters(object):
    '''
    
    '''
    def __init__(self):
        self.NodesToDelete = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToDelete)))
        for fieldname in self.NodesToDelete:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToDelete.append(DeleteNodesItem.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteNodesParameters(' + 'NodesToDelete:' + str(self.NodesToDelete) + ')'
    
    __repr__ = __str__
    
class DeleteNodesRequest(object):
    '''
    Delete one or more nodes from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteNodesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteNodesResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteNodesResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteNodesResponse(object):
    '''
    Delete one or more nodes from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteNodesResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteNodesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesItem(object):
    '''
    A request to delete a node from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesItem_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SourceNodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.TargetNodeId = ExpandedNodeId()
        self.DeleteBidirectional = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.SourceNodeId.to_binary())
        body.append(self.ReferenceTypeId.to_binary())
        body.append(pack_uatype('Boolean', self.IsForward))
        body.append(self.TargetNodeId.to_binary())
        body.append(pack_uatype('Boolean', self.DeleteBidirectional))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesItem()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SourceNodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        obj.TargetNodeId = ExpandedNodeId.from_binary(data)
        obj.DeleteBidirectional = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesItem(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SourceNodeId:' + str(self.SourceNodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'TargetNodeId:' + str(self.TargetNodeId) + ', '  + \
             'DeleteBidirectional:' + str(self.DeleteBidirectional) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ReferencesToDelete = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.ReferencesToDelete)))
        for fieldname in self.ReferencesToDelete:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ReferencesToDelete.append(DeleteReferencesItem.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteReferencesParameters(' + 'ReferencesToDelete:' + str(self.ReferencesToDelete) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesRequest(object):
    '''
    Delete one or more references from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteReferencesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteReferencesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteReferencesResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteReferencesResponse(object):
    '''
    Delete one or more references from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteReferencesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteReferencesResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteReferencesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteReferencesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteReferencesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ViewDescription(object):
    '''
    The view to browse.
    '''
    def __init__(self):
        self.ViewId = NodeId()
        self.Timestamp = DateTime()
        self.ViewVersion = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.ViewId.to_binary())
        packet.append(self.Timestamp.to_binary())
        packet.append(pack_uatype('UInt32', self.ViewVersion))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ViewDescription()
        obj.ViewId = NodeId.from_binary(data)
        obj.Timestamp = DateTime.from_binary(data)
        obj.ViewVersion = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ViewDescription(' + 'ViewId:' + str(self.ViewId) + ', '  + \
             'Timestamp:' + str(self.Timestamp) + ', '  + \
             'ViewVersion:' + str(self.ViewVersion) + ')'
    
    __repr__ = __str__
    
class BrowseDescription(object):
    '''
    A request to browse the the references from a node.
    '''
    def __init__(self):
        self.NodeId = NodeId()
        self.BrowseDirection = 0
        self.ReferenceTypeId = NodeId()
        self.IncludeSubtypes = True
        self.NodeClassMask = 0
        self.ResultMask = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.BrowseDirection))
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IncludeSubtypes))
        packet.append(pack_uatype('UInt32', self.NodeClassMask))
        packet.append(pack_uatype('UInt32', self.ResultMask))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseDescription()
        obj.NodeId = NodeId.from_binary(data)
        obj.BrowseDirection = unpack_uatype('UInt32', data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IncludeSubtypes = unpack_uatype('Boolean', data)
        obj.NodeClassMask = unpack_uatype('UInt32', data)
        obj.ResultMask = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'BrowseDescription(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'BrowseDirection:' + str(self.BrowseDirection) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', '  + \
             'NodeClassMask:' + str(self.NodeClassMask) + ', '  + \
             'ResultMask:' + str(self.ResultMask) + ')'
    
    __repr__ = __str__
    
class ReferenceDescription(object):
    '''
    The description of a reference.
    '''
    def __init__(self):
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.NodeId = ExpandedNodeId()
        self.BrowseName = QualifiedName()
        self.DisplayName = LocalizedText()
        self.NodeClass = 0
        self.TypeDefinition = ExpandedNodeId()
    
    def to_binary(self):
        packet = []
        packet.append(self.ReferenceTypeId.to_binary())
        packet.append(pack_uatype('Boolean', self.IsForward))
        packet.append(self.NodeId.to_binary())
        packet.append(self.BrowseName.to_binary())
        packet.append(self.DisplayName.to_binary())
        packet.append(pack_uatype('UInt32', self.NodeClass))
        packet.append(self.TypeDefinition.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReferenceDescription()
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        obj.NodeId = ExpandedNodeId.from_binary(data)
        obj.BrowseName = QualifiedName.from_binary(data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.NodeClass = unpack_uatype('UInt32', data)
        obj.TypeDefinition = ExpandedNodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReferenceDescription(' + 'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'BrowseName:' + str(self.BrowseName) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'NodeClass:' + str(self.NodeClass) + ', '  + \
             'TypeDefinition:' + str(self.TypeDefinition) + ')'
    
    __repr__ = __str__
    
class BrowseResult(object):
    '''
    The result of a browse operation.
    '''
    def __init__(self):
        self.StatusCode = StatusCode()
        self.ContinuationPoint = b''
        self.References = []
    
    def to_binary(self):
        packet = []
        packet.append(self.StatusCode.to_binary())
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        packet.append(struct.pack('<i', len(self.References)))
        for fieldname in self.References:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseResult()
        obj.StatusCode = StatusCode.from_binary(data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.References.append(ReferenceDescription.from_binary(data))
        return obj
    
    def __str__(self):
        return 'BrowseResult(' + 'StatusCode:' + str(self.StatusCode) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', '  + \
             'References:' + str(self.References) + ')'
    
    __repr__ = __str__
    
class BrowseParameters(object):
    '''
    
    '''
    def __init__(self):
        self.View = ViewDescription()
        self.RequestedMaxReferencesPerNode = 0
        self.NodesToBrowse = []
    
    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(pack_uatype('UInt32', self.RequestedMaxReferencesPerNode))
        packet.append(struct.pack('<i', len(self.NodesToBrowse)))
        for fieldname in self.NodesToBrowse:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseParameters()
        obj.View = ViewDescription.from_binary(data)
        obj.RequestedMaxReferencesPerNode = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToBrowse.append(BrowseDescription.from_binary(data))
        return obj
    
    def __str__(self):
        return 'BrowseParameters(' + 'View:' + str(self.View) + ', '  + \
             'RequestedMaxReferencesPerNode:' + str(self.RequestedMaxReferencesPerNode) + ', '  + \
             'NodesToBrowse:' + str(self.NodesToBrowse) + ')'
    
    __repr__ = __str__
    
class BrowseRequest(object):
    '''
    Browse the references for one or more nodes from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = BrowseParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class BrowseResponse(object):
    '''
    Browse the references for one or more nodes from the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(BrowseResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'BrowseResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class BrowseNextParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ReleaseContinuationPoints = True
        self.ContinuationPoints = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.ReleaseContinuationPoints))
        packet.append(struct.pack('<i', len(self.ContinuationPoints)))
        for fieldname in self.ContinuationPoints:
            packet.append(pack_uatype('ByteString', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseNextParameters()
        obj.ReleaseContinuationPoints = unpack_uatype('Boolean', data)
        obj.ContinuationPoints = unpack_uatype_array('ByteString', data)
        return obj
    
    def __str__(self):
        return 'BrowseNextParameters(' + 'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', '  + \
             'ContinuationPoints:' + str(self.ContinuationPoints) + ')'
    
    __repr__ = __str__
    
class BrowseNextRequest(object):
    '''
    Continues one or more browse operations.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = BrowseNextParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseNextRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = BrowseNextParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseNextRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class BrowseNextResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseNextResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(BrowseResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'BrowseNextResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class BrowseNextResponse(object):
    '''
    Continues one or more browse operations.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowseNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = BrowseNextResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowseNextResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = BrowseNextResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowseNextResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RelativePathElement(object):
    '''
    An element in a relative path.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RelativePathElement_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ReferenceTypeId = NodeId()
        self.IsInverse = True
        self.IncludeSubtypes = True
        self.TargetName = QualifiedName()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.ReferenceTypeId.to_binary())
        body.append(pack_uatype('Boolean', self.IsInverse))
        body.append(pack_uatype('Boolean', self.IncludeSubtypes))
        body.append(self.TargetName.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RelativePathElement()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsInverse = unpack_uatype('Boolean', data)
        obj.IncludeSubtypes = unpack_uatype('Boolean', data)
        obj.TargetName = QualifiedName.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RelativePathElement(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsInverse:' + str(self.IsInverse) + ', '  + \
             'IncludeSubtypes:' + str(self.IncludeSubtypes) + ', '  + \
             'TargetName:' + str(self.TargetName) + ')'
    
    __repr__ = __str__
    
class RelativePath(object):
    '''
    A relative path constructed from reference types and browse names.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RelativePath_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Elements = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.Elements)))
        for fieldname in self.Elements:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RelativePath()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Elements.append(RelativePathElement.from_binary(data))
        return obj
    
    def __str__(self):
        return 'RelativePath(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Elements:' + str(self.Elements) + ')'
    
    __repr__ = __str__
    
class BrowsePath(object):
    '''
    A request to translate a path into a node id.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowsePath_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StartingNode = NodeId()
        self.RelativePath = RelativePath()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StartingNode.to_binary())
        body.append(self.RelativePath.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowsePath()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StartingNode = NodeId.from_binary(data)
        obj.RelativePath = RelativePath.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BrowsePath(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StartingNode:' + str(self.StartingNode) + ', '  + \
             'RelativePath:' + str(self.RelativePath) + ')'
    
    __repr__ = __str__
    
class BrowsePathTarget(object):
    '''
    The target of the translated path.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowsePathTarget_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.TargetId = ExpandedNodeId()
        self.RemainingPathIndex = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.TargetId.to_binary())
        body.append(pack_uatype('UInt32', self.RemainingPathIndex))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowsePathTarget()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.TargetId = ExpandedNodeId.from_binary(data)
        obj.RemainingPathIndex = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'BrowsePathTarget(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'TargetId:' + str(self.TargetId) + ', '  + \
             'RemainingPathIndex:' + str(self.RemainingPathIndex) + ')'
    
    __repr__ = __str__
    
class BrowsePathResult(object):
    '''
    The result of a translate opearation.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BrowsePathResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.Targets = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(struct.pack('<i', len(self.Targets)))
        for fieldname in self.Targets:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BrowsePathResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Targets.append(BrowsePathTarget.from_binary(data))
        return obj
    
    def __str__(self):
        return 'BrowsePathResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'Targets:' + str(self.Targets) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.BrowsePaths = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.BrowsePaths)))
        for fieldname in self.BrowsePaths:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.BrowsePaths.append(BrowsePath.from_binary(data))
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsParameters(' + 'BrowsePaths:' + str(self.BrowsePaths) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsRequest(object):
    '''
    Translates one or more paths in the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TranslateBrowsePathsToNodeIdsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TranslateBrowsePathsToNodeIdsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(BrowsePathResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class TranslateBrowsePathsToNodeIdsResponse(object):
    '''
    Translates one or more paths in the server address space.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TranslateBrowsePathsToNodeIdsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TranslateBrowsePathsToNodeIdsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TranslateBrowsePathsToNodeIdsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TranslateBrowsePathsToNodeIdsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TranslateBrowsePathsToNodeIdsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RegisterNodesParameters(object):
    '''
    
    '''
    def __init__(self):
        self.NodesToRegister = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToRegister)))
        for fieldname in self.NodesToRegister:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToRegister.append(NodeId.from_binary(data))
        return obj
    
    def __str__(self):
        return 'RegisterNodesParameters(' + 'NodesToRegister:' + str(self.NodesToRegister) + ')'
    
    __repr__ = __str__
    
class RegisterNodesRequest(object):
    '''
    Registers one or more nodes for repeated use within a session.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RegisterNodesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RegisterNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RegisterNodesResult(object):
    '''
    
    '''
    def __init__(self):
        self.RegisteredNodeIds = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.RegisteredNodeIds)))
        for fieldname in self.RegisteredNodeIds:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterNodesResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.RegisteredNodeIds.append(NodeId.from_binary(data))
        return obj
    
    def __str__(self):
        return 'RegisterNodesResult(' + 'RegisteredNodeIds:' + str(self.RegisteredNodeIds) + ')'
    
    __repr__ = __str__
    
class RegisterNodesResponse(object):
    '''
    Registers one or more nodes for repeated use within a session.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RegisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RegisterNodesResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RegisterNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = RegisterNodesResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RegisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UnregisterNodesParameters(object):
    '''
    
    '''
    def __init__(self):
        self.NodesToUnregister = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToUnregister)))
        for fieldname in self.NodesToUnregister:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToUnregister.append(NodeId.from_binary(data))
        return obj
    
    def __str__(self):
        return 'UnregisterNodesParameters(' + 'NodesToUnregister:' + str(self.NodesToUnregister) + ')'
    
    __repr__ = __str__
    
class UnregisterNodesRequest(object):
    '''
    Unregisters one or more previously registered nodes.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = UnregisterNodesParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = UnregisterNodesParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UnregisterNodesRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class UnregisterNodesResponse(object):
    '''
    Unregisters one or more previously registered nodes.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UnregisterNodesResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UnregisterNodesResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        return obj
    
    def __str__(self):
        return 'UnregisterNodesResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ')'
    
    __repr__ = __str__
    
class EndpointConfiguration(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EndpointConfiguration_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.OperationTimeout = 0
        self.UseBinaryEncoding = True
        self.MaxStringLength = 0
        self.MaxByteStringLength = 0
        self.MaxArrayLength = 0
        self.MaxMessageSize = 0
        self.MaxBufferSize = 0
        self.ChannelLifetime = 0
        self.SecurityTokenLifetime = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Int32', self.OperationTimeout))
        body.append(pack_uatype('Boolean', self.UseBinaryEncoding))
        body.append(pack_uatype('Int32', self.MaxStringLength))
        body.append(pack_uatype('Int32', self.MaxByteStringLength))
        body.append(pack_uatype('Int32', self.MaxArrayLength))
        body.append(pack_uatype('Int32', self.MaxMessageSize))
        body.append(pack_uatype('Int32', self.MaxBufferSize))
        body.append(pack_uatype('Int32', self.ChannelLifetime))
        body.append(pack_uatype('Int32', self.SecurityTokenLifetime))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EndpointConfiguration()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.OperationTimeout = unpack_uatype('Int32', data)
        obj.UseBinaryEncoding = unpack_uatype('Boolean', data)
        obj.MaxStringLength = unpack_uatype('Int32', data)
        obj.MaxByteStringLength = unpack_uatype('Int32', data)
        obj.MaxArrayLength = unpack_uatype('Int32', data)
        obj.MaxMessageSize = unpack_uatype('Int32', data)
        obj.MaxBufferSize = unpack_uatype('Int32', data)
        obj.ChannelLifetime = unpack_uatype('Int32', data)
        obj.SecurityTokenLifetime = unpack_uatype('Int32', data)
        return obj
    
    def __str__(self):
        return 'EndpointConfiguration(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'OperationTimeout:' + str(self.OperationTimeout) + ', '  + \
             'UseBinaryEncoding:' + str(self.UseBinaryEncoding) + ', '  + \
             'MaxStringLength:' + str(self.MaxStringLength) + ', '  + \
             'MaxByteStringLength:' + str(self.MaxByteStringLength) + ', '  + \
             'MaxArrayLength:' + str(self.MaxArrayLength) + ', '  + \
             'MaxMessageSize:' + str(self.MaxMessageSize) + ', '  + \
             'MaxBufferSize:' + str(self.MaxBufferSize) + ', '  + \
             'ChannelLifetime:' + str(self.ChannelLifetime) + ', '  + \
             'SecurityTokenLifetime:' + str(self.SecurityTokenLifetime) + ')'
    
    __repr__ = __str__
    
class SupportedProfile(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SupportedProfile_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.OrganizationUri = ''
        self.ProfileId = ''
        self.ComplianceTool = ''
        self.ComplianceDate = DateTime()
        self.ComplianceLevel = 0
        self.UnsupportedUnitIds = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.OrganizationUri))
        body.append(pack_uatype('String', self.ProfileId))
        body.append(pack_uatype('String', self.ComplianceTool))
        body.append(self.ComplianceDate.to_binary())
        body.append(pack_uatype('UInt32', self.ComplianceLevel))
        body.append(struct.pack('<i', len(self.UnsupportedUnitIds)))
        for fieldname in self.UnsupportedUnitIds:
            body.append(pack_uatype('String', fieldname))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SupportedProfile()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.OrganizationUri = unpack_uatype('String', data)
        obj.ProfileId = unpack_uatype('String', data)
        obj.ComplianceTool = unpack_uatype('String', data)
        obj.ComplianceDate = DateTime.from_binary(data)
        obj.ComplianceLevel = unpack_uatype('UInt32', data)
        obj.UnsupportedUnitIds = unpack_uatype_array('String', data)
        return obj
    
    def __str__(self):
        return 'SupportedProfile(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'OrganizationUri:' + str(self.OrganizationUri) + ', '  + \
             'ProfileId:' + str(self.ProfileId) + ', '  + \
             'ComplianceTool:' + str(self.ComplianceTool) + ', '  + \
             'ComplianceDate:' + str(self.ComplianceDate) + ', '  + \
             'ComplianceLevel:' + str(self.ComplianceLevel) + ', '  + \
             'UnsupportedUnitIds:' + str(self.UnsupportedUnitIds) + ')'
    
    __repr__ = __str__
    
class SoftwareCertificate(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SoftwareCertificate_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ProductName = ''
        self.ProductUri = ''
        self.VendorName = ''
        self.VendorProductCertificate = b''
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = DateTime()
        self.IssuedBy = ''
        self.IssueDate = DateTime()
        self.SupportedProfiles = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.ProductName))
        body.append(pack_uatype('String', self.ProductUri))
        body.append(pack_uatype('String', self.VendorName))
        body.append(pack_uatype('ByteString', self.VendorProductCertificate))
        body.append(pack_uatype('String', self.SoftwareVersion))
        body.append(pack_uatype('String', self.BuildNumber))
        body.append(self.BuildDate.to_binary())
        body.append(pack_uatype('String', self.IssuedBy))
        body.append(self.IssueDate.to_binary())
        body.append(struct.pack('<i', len(self.SupportedProfiles)))
        for fieldname in self.SupportedProfiles:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SoftwareCertificate()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ProductName = unpack_uatype('String', data)
        obj.ProductUri = unpack_uatype('String', data)
        obj.VendorName = unpack_uatype('String', data)
        obj.VendorProductCertificate = unpack_uatype('ByteString', data)
        obj.SoftwareVersion = unpack_uatype('String', data)
        obj.BuildNumber = unpack_uatype('String', data)
        obj.BuildDate = DateTime.from_binary(data)
        obj.IssuedBy = unpack_uatype('String', data)
        obj.IssueDate = DateTime.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.SupportedProfiles.append(SupportedProfile.from_binary(data))
        return obj
    
    def __str__(self):
        return 'SoftwareCertificate(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ProductName:' + str(self.ProductName) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'VendorName:' + str(self.VendorName) + ', '  + \
             'VendorProductCertificate:' + str(self.VendorProductCertificate) + ', '  + \
             'SoftwareVersion:' + str(self.SoftwareVersion) + ', '  + \
             'BuildNumber:' + str(self.BuildNumber) + ', '  + \
             'BuildDate:' + str(self.BuildDate) + ', '  + \
             'IssuedBy:' + str(self.IssuedBy) + ', '  + \
             'IssueDate:' + str(self.IssueDate) + ', '  + \
             'SupportedProfiles:' + str(self.SupportedProfiles) + ')'
    
    __repr__ = __str__
    
class QueryDataDescription(object):
    '''
    
    '''
    def __init__(self):
        self.RelativePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''
    
    def to_binary(self):
        packet = []
        packet.append(self.RelativePath.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryDataDescription()
        obj.RelativePath = RelativePath.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'QueryDataDescription(' + 'RelativePath:' + str(self.RelativePath) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ')'
    
    __repr__ = __str__
    
class NodeTypeDescription(object):
    '''
    
    '''
    def __init__(self):
        self.TypeDefinitionNode = ExpandedNodeId()
        self.IncludeSubTypes = True
        self.DataToReturn = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeDefinitionNode.to_binary())
        packet.append(pack_uatype('Boolean', self.IncludeSubTypes))
        packet.append(struct.pack('<i', len(self.DataToReturn)))
        for fieldname in self.DataToReturn:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NodeTypeDescription()
        obj.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        obj.IncludeSubTypes = unpack_uatype('Boolean', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DataToReturn.append(QueryDataDescription.from_binary(data))
        return obj
    
    def __str__(self):
        return 'NodeTypeDescription(' + 'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', '  + \
             'IncludeSubTypes:' + str(self.IncludeSubTypes) + ', '  + \
             'DataToReturn:' + str(self.DataToReturn) + ')'
    
    __repr__ = __str__
    
class QueryDataSet(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryDataSet_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = ExpandedNodeId()
        self.TypeDefinitionNode = ExpandedNodeId()
        self.Values = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(self.TypeDefinitionNode.to_binary())
        body.append(struct.pack('<i', len(self.Values)))
        for fieldname in self.Values:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryDataSet()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = ExpandedNodeId.from_binary(data)
        obj.TypeDefinitionNode = ExpandedNodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Values.append(Variant.from_binary(data))
        return obj
    
    def __str__(self):
        return 'QueryDataSet(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'TypeDefinitionNode:' + str(self.TypeDefinitionNode) + ', '  + \
             'Values:' + str(self.Values) + ')'
    
    __repr__ = __str__
    
class NodeReference(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.NodeReference_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.ReferenceTypeId = NodeId()
        self.IsForward = True
        self.ReferencedNodeIds = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(self.ReferenceTypeId.to_binary())
        body.append(pack_uatype('Boolean', self.IsForward))
        body.append(struct.pack('<i', len(self.ReferencedNodeIds)))
        for fieldname in self.ReferencedNodeIds:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NodeReference()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.ReferenceTypeId = NodeId.from_binary(data)
        obj.IsForward = unpack_uatype('Boolean', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ReferencedNodeIds.append(NodeId.from_binary(data))
        return obj
    
    def __str__(self):
        return 'NodeReference(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'ReferenceTypeId:' + str(self.ReferenceTypeId) + ', '  + \
             'IsForward:' + str(self.IsForward) + ', '  + \
             'ReferencedNodeIds:' + str(self.ReferencedNodeIds) + ')'
    
    __repr__ = __str__
    
class ContentFilterElement(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ContentFilterElement_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.FilterOperator = 0
        self.FilterOperands = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.FilterOperator))
        body.append(struct.pack('<i', len(self.FilterOperands)))
        for fieldname in self.FilterOperands:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilterElement()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.FilterOperator = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.FilterOperands.append(ExtensionObject.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ContentFilterElement(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'FilterOperator:' + str(self.FilterOperator) + ', '  + \
             'FilterOperands:' + str(self.FilterOperands) + ')'
    
    __repr__ = __str__
    
class ContentFilter(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ContentFilter_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Elements = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.Elements)))
        for fieldname in self.Elements:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilter()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Elements.append(ContentFilterElement.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ContentFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Elements:' + str(self.Elements) + ')'
    
    __repr__ = __str__
    
class ElementOperand(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ElementOperand_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Index = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.Index))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ElementOperand()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Index = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ElementOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Index:' + str(self.Index) + ')'
    
    __repr__ = __str__
    
class LiteralOperand(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.LiteralOperand_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Value = Variant()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.Value.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = LiteralOperand()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Value = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'LiteralOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class AttributeOperand(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AttributeOperand_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.Alias = ''
        self.BrowsePath = RelativePath()
        self.AttributeId = 0
        self.IndexRange = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('String', self.Alias))
        body.append(self.BrowsePath.to_binary())
        body.append(pack_uatype('UInt32', self.AttributeId))
        body.append(pack_uatype('String', self.IndexRange))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AttributeOperand()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.Alias = unpack_uatype('String', data)
        obj.BrowsePath = RelativePath.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'AttributeOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'Alias:' + str(self.Alias) + ', '  + \
             'BrowsePath:' + str(self.BrowsePath) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ')'
    
    __repr__ = __str__
    
class SimpleAttributeOperand(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SimpleAttributeOperand_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.TypeDefinitionId = NodeId()
        self.BrowsePath = []
        self.AttributeId = 0
        self.IndexRange = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.TypeDefinitionId.to_binary())
        body.append(struct.pack('<i', len(self.BrowsePath)))
        for fieldname in self.BrowsePath:
            body.append(fieldname.to_binary())
        body.append(pack_uatype('UInt32', self.AttributeId))
        body.append(pack_uatype('String', self.IndexRange))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SimpleAttributeOperand()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.TypeDefinitionId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.BrowsePath.append(QualifiedName.from_binary(data))
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'SimpleAttributeOperand(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'TypeDefinitionId:' + str(self.TypeDefinitionId) + ', '  + \
             'BrowsePath:' + str(self.BrowsePath) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ')'
    
    __repr__ = __str__
    
class ContentFilterElementResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ContentFilterElementResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.OperandStatusCodes = []
        self.OperandDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(struct.pack('<i', len(self.OperandStatusCodes)))
        for fieldname in self.OperandStatusCodes:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.OperandDiagnosticInfos)))
        for fieldname in self.OperandDiagnosticInfos:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilterElementResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.OperandStatusCodes.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.OperandDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ContentFilterElementResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'OperandStatusCodes:' + str(self.OperandStatusCodes) + ', '  + \
             'OperandDiagnosticInfos:' + str(self.OperandDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ContentFilterResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ContentFilterResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ElementResults = []
        self.ElementDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.ElementResults)))
        for fieldname in self.ElementResults:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.ElementDiagnosticInfos)))
        for fieldname in self.ElementDiagnosticInfos:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ContentFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ElementResults.append(ContentFilterElementResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ElementDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ContentFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ElementResults:' + str(self.ElementResults) + ', '  + \
             'ElementDiagnosticInfos:' + str(self.ElementDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ParsingResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ParsingResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.DataStatusCodes = []
        self.DataDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(struct.pack('<i', len(self.DataStatusCodes)))
        for fieldname in self.DataStatusCodes:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.DataDiagnosticInfos)))
        for fieldname in self.DataDiagnosticInfos:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ParsingResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DataStatusCodes.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DataDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ParsingResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DataStatusCodes:' + str(self.DataStatusCodes) + ', '  + \
             'DataDiagnosticInfos:' + str(self.DataDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class QueryFirstParameters(object):
    '''
    
    '''
    def __init__(self):
        self.View = ViewDescription()
        self.NodeTypes = []
        self.Filter = ContentFilter()
        self.MaxDataSetsToReturn = 0
        self.MaxReferencesToReturn = 0
    
    def to_binary(self):
        packet = []
        packet.append(self.View.to_binary())
        packet.append(struct.pack('<i', len(self.NodeTypes)))
        for fieldname in self.NodeTypes:
            packet.append(fieldname.to_binary())
        packet.append(self.Filter.to_binary())
        packet.append(pack_uatype('UInt32', self.MaxDataSetsToReturn))
        packet.append(pack_uatype('UInt32', self.MaxReferencesToReturn))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryFirstParameters()
        obj.View = ViewDescription.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodeTypes.append(NodeTypeDescription.from_binary(data))
        obj.Filter = ContentFilter.from_binary(data)
        obj.MaxDataSetsToReturn = unpack_uatype('UInt32', data)
        obj.MaxReferencesToReturn = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'QueryFirstParameters(' + 'View:' + str(self.View) + ', '  + \
             'NodeTypes:' + str(self.NodeTypes) + ', '  + \
             'Filter:' + str(self.Filter) + ', '  + \
             'MaxDataSetsToReturn:' + str(self.MaxDataSetsToReturn) + ', '  + \
             'MaxReferencesToReturn:' + str(self.MaxReferencesToReturn) + ')'
    
    __repr__ = __str__
    
class QueryFirstRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryFirstParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryFirstRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = QueryFirstParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryFirstRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class QueryFirstResult(object):
    '''
    
    '''
    def __init__(self):
        self.QueryDataSets = []
        self.ContinuationPoint = b''
        self.ParsingResults = []
        self.DiagnosticInfos = []
        self.FilterResult = ContentFilterResult()
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.QueryDataSets)))
        for fieldname in self.QueryDataSets:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        packet.append(struct.pack('<i', len(self.ParsingResults)))
        for fieldname in self.ParsingResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(self.FilterResult.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryFirstResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.QueryDataSets.append(QueryDataSet.from_binary(data))
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ParsingResults.append(ParsingResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        obj.FilterResult = ContentFilterResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryFirstResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', '  + \
             'ParsingResults:' + str(self.ParsingResults) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ', '  + \
             'FilterResult:' + str(self.FilterResult) + ')'
    
    __repr__ = __str__
    
class QueryFirstResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryFirstResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryFirstResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryFirstResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = QueryFirstResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryFirstResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class QueryNextParameters(object):
    '''
    
    '''
    def __init__(self):
        self.ReleaseContinuationPoint = True
        self.ContinuationPoint = b''
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.ReleaseContinuationPoint))
        packet.append(pack_uatype('ByteString', self.ContinuationPoint))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryNextParameters()
        obj.ReleaseContinuationPoint = unpack_uatype('Boolean', data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'QueryNextParameters(' + 'ReleaseContinuationPoint:' + str(self.ReleaseContinuationPoint) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ')'
    
    __repr__ = __str__
    
class QueryNextRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = QueryNextParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryNextRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = QueryNextParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryNextRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class QueryNextResult(object):
    '''
    
    '''
    def __init__(self):
        self.QueryDataSets = []
        self.RevisedContinuationPoint = b''
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.QueryDataSets)))
        for fieldname in self.QueryDataSets:
            packet.append(fieldname.to_binary())
        packet.append(pack_uatype('ByteString', self.RevisedContinuationPoint))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryNextResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.QueryDataSets.append(QueryDataSet.from_binary(data))
        obj.RevisedContinuationPoint = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'QueryNextResult(' + 'QueryDataSets:' + str(self.QueryDataSets) + ', '  + \
             'RevisedContinuationPoint:' + str(self.RevisedContinuationPoint) + ')'
    
    __repr__ = __str__
    
class QueryNextResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.QueryNextResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = QueryNextResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = QueryNextResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = QueryNextResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'QueryNextResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ReadValueId(object):
    '''
    
    '''
    def __init__(self):
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
    
    def to_binary(self):
        packet = []
        packet.append(self.NodeId.to_binary())
        packet.append(pack_uatype('UInt32', self.AttributeId))
        packet.append(pack_uatype('String', self.IndexRange))
        packet.append(self.DataEncoding.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadValueId()
        obj.NodeId = NodeId.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        obj.DataEncoding = QualifiedName.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadValueId(' + 'NodeId:' + str(self.NodeId) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ', '  + \
             'DataEncoding:' + str(self.DataEncoding) + ')'
    
    __repr__ = __str__
    
class ReadParameters(object):
    '''
    
    '''
    def __init__(self):
        self.MaxAge = 0
        self.TimestampsToReturn = 0
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.MaxAge))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.NodesToRead)))
        for fieldname in self.NodesToRead:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadParameters()
        obj.MaxAge = unpack_uatype('Double', data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToRead.append(ReadValueId.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ReadParameters(' + 'MaxAge:' + str(self.MaxAge) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'NodesToRead:' + str(self.NodesToRead) + ')'
    
    __repr__ = __str__
    
class ReadRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ReadParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ReadParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ReadResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(DataValue.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ReadResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class HistoryReadValueId(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadValueId_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.IndexRange = ''
        self.DataEncoding = QualifiedName()
        self.ContinuationPoint = b''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('String', self.IndexRange))
        body.append(self.DataEncoding.to_binary())
        body.append(pack_uatype('ByteString', self.ContinuationPoint))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadValueId()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.IndexRange = unpack_uatype('String', data)
        obj.DataEncoding = QualifiedName.from_binary(data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'HistoryReadValueId(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ', '  + \
             'DataEncoding:' + str(self.DataEncoding) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ')'
    
    __repr__ = __str__
    
class HistoryReadResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.ContinuationPoint = b''
        self.HistoryData = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(pack_uatype('ByteString', self.ContinuationPoint))
        body.append(self.HistoryData.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.ContinuationPoint = unpack_uatype('ByteString', data)
        obj.HistoryData = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'ContinuationPoint:' + str(self.ContinuationPoint) + ', '  + \
             'HistoryData:' + str(self.HistoryData) + ')'
    
    __repr__ = __str__
    
class HistoryReadDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadDetails_Encoding_DefaultBinary)
        self.Encoding = 0
        self.Body = b''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Body: 
            packet.append(pack_uatype('ByteString', self.Body))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Body = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'HistoryReadDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class ReadEventDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadEventDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NumValuesPerNode = 0
        self.StartTime = DateTime()
        self.EndTime = DateTime()
        self.Filter = EventFilter()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.NumValuesPerNode))
        body.append(self.StartTime.to_binary())
        body.append(self.EndTime.to_binary())
        body.append(self.Filter.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadEventDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NumValuesPerNode = unpack_uatype('UInt32', data)
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        obj.Filter = EventFilter.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadEventDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ', '  + \
             'Filter:' + str(self.Filter) + ')'
    
    __repr__ = __str__
    
class ReadRawModifiedDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadRawModifiedDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.IsReadModified = True
        self.StartTime = DateTime()
        self.EndTime = DateTime()
        self.NumValuesPerNode = 0
        self.ReturnBounds = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Boolean', self.IsReadModified))
        body.append(self.StartTime.to_binary())
        body.append(self.EndTime.to_binary())
        body.append(pack_uatype('UInt32', self.NumValuesPerNode))
        body.append(pack_uatype('Boolean', self.ReturnBounds))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadRawModifiedDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.IsReadModified = unpack_uatype('Boolean', data)
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        obj.NumValuesPerNode = unpack_uatype('UInt32', data)
        obj.ReturnBounds = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'ReadRawModifiedDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'IsReadModified:' + str(self.IsReadModified) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ', '  + \
             'NumValuesPerNode:' + str(self.NumValuesPerNode) + ', '  + \
             'ReturnBounds:' + str(self.ReturnBounds) + ')'
    
    __repr__ = __str__
    
class ReadProcessedDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadProcessedDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StartTime = DateTime()
        self.EndTime = DateTime()
        self.ProcessingInterval = 0
        self.AggregateType = []
        self.AggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StartTime.to_binary())
        body.append(self.EndTime.to_binary())
        body.append(pack_uatype('Double', self.ProcessingInterval))
        body.append(struct.pack('<i', len(self.AggregateType)))
        for fieldname in self.AggregateType:
            body.append(fieldname.to_binary())
        body.append(self.AggregateConfiguration.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadProcessedDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        obj.ProcessingInterval = unpack_uatype('Double', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.AggregateType.append(NodeId.from_binary(data))
        obj.AggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ReadProcessedDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ', '  + \
             'ProcessingInterval:' + str(self.ProcessingInterval) + ', '  + \
             'AggregateType:' + str(self.AggregateType) + ', '  + \
             'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'
    
    __repr__ = __str__
    
class ReadAtTimeDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ReadAtTimeDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ReqTimes = []
        self.UseSimpleBounds = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.ReqTimes)))
        for fieldname in self.ReqTimes:
            body.append(fieldname.to_binary())
        body.append(pack_uatype('Boolean', self.UseSimpleBounds))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ReadAtTimeDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ReqTimes.append(DateTime.from_binary(data))
        obj.UseSimpleBounds = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'ReadAtTimeDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ReqTimes:' + str(self.ReqTimes) + ', '  + \
             'UseSimpleBounds:' + str(self.UseSimpleBounds) + ')'
    
    __repr__ = __str__
    
class HistoryData(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryData_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.DataValues = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.DataValues)))
        for fieldname in self.DataValues:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryData()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DataValues.append(DataValue.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryData(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'DataValues:' + str(self.DataValues) + ')'
    
    __repr__ = __str__
    
class ModificationInfo(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModificationInfo_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ModificationTime = DateTime()
        self.UpdateType = 0
        self.UserName = ''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.ModificationTime.to_binary())
        body.append(pack_uatype('UInt32', self.UpdateType))
        body.append(pack_uatype('String', self.UserName))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModificationInfo()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ModificationTime = DateTime.from_binary(data)
        obj.UpdateType = unpack_uatype('UInt32', data)
        obj.UserName = unpack_uatype('String', data)
        return obj
    
    def __str__(self):
        return 'ModificationInfo(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ModificationTime:' + str(self.ModificationTime) + ', '  + \
             'UpdateType:' + str(self.UpdateType) + ', '  + \
             'UserName:' + str(self.UserName) + ')'
    
    __repr__ = __str__
    
class HistoryModifiedData(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryModifiedData_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.DataValues = []
        self.ModificationInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.DataValues)))
        for fieldname in self.DataValues:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.ModificationInfos)))
        for fieldname in self.ModificationInfos:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryModifiedData()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DataValues.append(DataValue.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ModificationInfos.append(ModificationInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryModifiedData(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'DataValues:' + str(self.DataValues) + ', '  + \
             'ModificationInfos:' + str(self.ModificationInfos) + ')'
    
    __repr__ = __str__
    
class HistoryEvent(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryEvent_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Events = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.Events)))
        for fieldname in self.Events:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryEvent()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Events.append(HistoryEventFieldList.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryEvent(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Events:' + str(self.Events) + ')'
    
    __repr__ = __str__
    
class HistoryReadParameters(object):
    '''
    
    '''
    def __init__(self):
        self.HistoryReadDetails = ExtensionObject()
        self.TimestampsToReturn = 0
        self.ReleaseContinuationPoints = True
        self.NodesToRead = []
    
    def to_binary(self):
        packet = []
        packet.append(self.HistoryReadDetails.to_binary())
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(pack_uatype('Boolean', self.ReleaseContinuationPoints))
        packet.append(struct.pack('<i', len(self.NodesToRead)))
        for fieldname in self.NodesToRead:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadParameters()
        obj.HistoryReadDetails = ExtensionObject.from_binary(data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        obj.ReleaseContinuationPoints = unpack_uatype('Boolean', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToRead.append(HistoryReadValueId.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryReadParameters(' + 'HistoryReadDetails:' + str(self.HistoryReadDetails) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'ReleaseContinuationPoints:' + str(self.ReleaseContinuationPoints) + ', '  + \
             'NodesToRead:' + str(self.NodesToRead) + ')'
    
    __repr__ = __str__
    
class HistoryReadRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryReadParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = HistoryReadParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryReadRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryReadResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryReadResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryReadResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(HistoryReadResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryReadResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class WriteValue(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteValue_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.AttributeId = 0
        self.IndexRange = ''
        self.Value = DataValue()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('UInt32', self.AttributeId))
        body.append(pack_uatype('String', self.IndexRange))
        body.append(self.Value.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteValue()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.AttributeId = unpack_uatype('UInt32', data)
        obj.IndexRange = unpack_uatype('String', data)
        obj.Value = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteValue(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'AttributeId:' + str(self.AttributeId) + ', '  + \
             'IndexRange:' + str(self.IndexRange) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class WriteParameters(object):
    '''
    
    '''
    def __init__(self):
        self.NodesToWrite = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.NodesToWrite)))
        for fieldname in self.NodesToWrite:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodesToWrite.append(WriteValue.from_binary(data))
        return obj
    
    def __str__(self):
        return 'WriteParameters(' + 'NodesToWrite:' + str(self.NodesToWrite) + ')'
    
    __repr__ = __str__
    
class WriteRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = WriteParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = WriteParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class WriteResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'WriteResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class WriteResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.WriteResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = WriteResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = WriteResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = WriteResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'WriteResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ')'
    
    __repr__ = __str__
    
class UpdateDataDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UpdateDataDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('UInt32', self.PerformInsertReplace))
        body.append(struct.pack('<i', len(self.UpdateValues)))
        for fieldname in self.UpdateValues:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UpdateDataDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.PerformInsertReplace = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.UpdateValues.append(DataValue.from_binary(data))
        return obj
    
    def __str__(self):
        return 'UpdateDataDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', '  + \
             'UpdateValues:' + str(self.UpdateValues) + ')'
    
    __repr__ = __str__
    
class UpdateStructureDataDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UpdateStructureDataDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.UpdateValues = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('UInt32', self.PerformInsertReplace))
        body.append(struct.pack('<i', len(self.UpdateValues)))
        for fieldname in self.UpdateValues:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UpdateStructureDataDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.PerformInsertReplace = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.UpdateValues.append(DataValue.from_binary(data))
        return obj
    
    def __str__(self):
        return 'UpdateStructureDataDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', '  + \
             'UpdateValues:' + str(self.UpdateValues) + ')'
    
    __repr__ = __str__
    
class UpdateEventDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.UpdateEventDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.PerformInsertReplace = 0
        self.Filter = EventFilter()
        self.EventData = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('UInt32', self.PerformInsertReplace))
        body.append(self.Filter.to_binary())
        body.append(struct.pack('<i', len(self.EventData)))
        for fieldname in self.EventData:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = UpdateEventDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.PerformInsertReplace = unpack_uatype('UInt32', data)
        obj.Filter = EventFilter.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.EventData.append(HistoryEventFieldList.from_binary(data))
        return obj
    
    def __str__(self):
        return 'UpdateEventDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'PerformInsertReplace:' + str(self.PerformInsertReplace) + ', '  + \
             'Filter:' + str(self.Filter) + ', '  + \
             'EventData:' + str(self.EventData) + ')'
    
    __repr__ = __str__
    
class DeleteRawModifiedDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteRawModifiedDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.IsDeleteModified = True
        self.StartTime = DateTime()
        self.EndTime = DateTime()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(pack_uatype('Boolean', self.IsDeleteModified))
        body.append(self.StartTime.to_binary())
        body.append(self.EndTime.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteRawModifiedDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.IsDeleteModified = unpack_uatype('Boolean', data)
        obj.StartTime = DateTime.from_binary(data)
        obj.EndTime = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteRawModifiedDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'IsDeleteModified:' + str(self.IsDeleteModified) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'EndTime:' + str(self.EndTime) + ')'
    
    __repr__ = __str__
    
class DeleteAtTimeDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteAtTimeDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.ReqTimes = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(struct.pack('<i', len(self.ReqTimes)))
        for fieldname in self.ReqTimes:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteAtTimeDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ReqTimes.append(DateTime.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteAtTimeDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'ReqTimes:' + str(self.ReqTimes) + ')'
    
    __repr__ = __str__
    
class DeleteEventDetails(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteEventDetails_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NodeId = NodeId()
        self.EventIds = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.NodeId.to_binary())
        body.append(struct.pack('<i', len(self.EventIds)))
        for fieldname in self.EventIds:
            body.append(pack_uatype('ByteString', fieldname))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteEventDetails()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NodeId = NodeId.from_binary(data)
        obj.EventIds = unpack_uatype_array('ByteString', data)
        return obj
    
    def __str__(self):
        return 'DeleteEventDetails(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'EventIds:' + str(self.EventIds) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.OperationResults = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(struct.pack('<i', len(self.OperationResults)))
        for fieldname in self.OperationResults:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.OperationResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryUpdateResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'OperationResults:' + str(self.OperationResults) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateEventResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateEventResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.EventFilterResult = EventFilterResult()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(self.EventFilterResult.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateEventResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.EventFilterResult = EventFilterResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateEventResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'EventFilterResult:' + str(self.EventFilterResult) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateParameters(object):
    '''
    
    '''
    def __init__(self):
        self.HistoryUpdateDetails = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.HistoryUpdateDetails)))
        for fieldname in self.HistoryUpdateDetails:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.HistoryUpdateDetails.append(ExtensionObject.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryUpdateParameters(' + 'HistoryUpdateDetails:' + str(self.HistoryUpdateDetails) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = HistoryUpdateParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = HistoryUpdateParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'HistoryUpdateRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class HistoryUpdateResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryUpdateResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryUpdateResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(HistoryUpdateResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryUpdateResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class CallMethodParameters(object):
    '''
    
    '''
    def __init__(self):
        self.MethodId = NodeId()
        self.InputArguments = []
    
    def to_binary(self):
        packet = []
        packet.append(self.MethodId.to_binary())
        packet.append(struct.pack('<i', len(self.InputArguments)))
        for fieldname in self.InputArguments:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallMethodParameters()
        obj.MethodId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.InputArguments.append(Variant.from_binary(data))
        return obj
    
    def __str__(self):
        return 'CallMethodParameters(' + 'MethodId:' + str(self.MethodId) + ', '  + \
             'InputArguments:' + str(self.InputArguments) + ')'
    
    __repr__ = __str__
    
class CallMethodRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallMethodRequest_Encoding_DefaultBinary)
        self.ObjectId = NodeId()
        self.Parameters = CallMethodParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ObjectId.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallMethodRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.ObjectId = NodeId.from_binary(data)
        obj.Parameters = CallMethodParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallMethodRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ObjectId:' + str(self.ObjectId) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CallMethodResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallMethodResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.InputArgumentResults = []
        self.InputArgumentDiagnosticInfos = []
        self.OutputArguments = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(struct.pack('<i', len(self.InputArgumentResults)))
        for fieldname in self.InputArgumentResults:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.InputArgumentDiagnosticInfos)))
        for fieldname in self.InputArgumentDiagnosticInfos:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.OutputArguments)))
        for fieldname in self.OutputArguments:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallMethodResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.InputArgumentResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.InputArgumentDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.OutputArguments.append(Variant.from_binary(data))
        return obj
    
    def __str__(self):
        return 'CallMethodResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'InputArgumentResults:' + str(self.InputArgumentResults) + ', '  + \
             'InputArgumentDiagnosticInfos:' + str(self.InputArgumentDiagnosticInfos) + ', '  + \
             'OutputArguments:' + str(self.OutputArguments) + ')'
    
    __repr__ = __str__
    
class CallParameters(object):
    '''
    
    '''
    def __init__(self):
        self.MethodsToCall = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.MethodsToCall)))
        for fieldname in self.MethodsToCall:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.MethodsToCall.append(CallMethodRequest.from_binary(data))
        return obj
    
    def __str__(self):
        return 'CallParameters(' + 'MethodsToCall:' + str(self.MethodsToCall) + ')'
    
    __repr__ = __str__
    
class CallRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CallParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CallParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CallResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(CallMethodResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'CallResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class CallResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CallResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CallResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CallResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CallResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CallResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class MonitoringFilter(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoringFilter_Encoding_DefaultBinary)
        self.Encoding = 0
        self.Body = b''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Body: 
            packet.append(pack_uatype('ByteString', self.Body))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoringFilter()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Body = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'MonitoringFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class DataChangeFilter(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DataChangeFilter_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Trigger = 0
        self.DeadbandType = 0
        self.DeadbandValue = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.Trigger))
        body.append(pack_uatype('UInt32', self.DeadbandType))
        body.append(pack_uatype('Double', self.DeadbandValue))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataChangeFilter()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Trigger = unpack_uatype('UInt32', data)
        obj.DeadbandType = unpack_uatype('UInt32', data)
        obj.DeadbandValue = unpack_uatype('Double', data)
        return obj
    
    def __str__(self):
        return 'DataChangeFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Trigger:' + str(self.Trigger) + ', '  + \
             'DeadbandType:' + str(self.DeadbandType) + ', '  + \
             'DeadbandValue:' + str(self.DeadbandValue) + ')'
    
    __repr__ = __str__
    
class EventFilter(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EventFilter_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SelectClauses = []
        self.WhereClause = ContentFilter()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.SelectClauses)))
        for fieldname in self.SelectClauses:
            body.append(fieldname.to_binary())
        body.append(self.WhereClause.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventFilter()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.SelectClauses.append(SimpleAttributeOperand.from_binary(data))
        obj.WhereClause = ContentFilter.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EventFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SelectClauses:' + str(self.SelectClauses) + ', '  + \
             'WhereClause:' + str(self.WhereClause) + ')'
    
    __repr__ = __str__
    
class AggregateConfiguration(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AggregateConfiguration_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.UseServerCapabilitiesDefaults = True
        self.TreatUncertainAsBad = True
        self.PercentDataBad = 0
        self.PercentDataGood = 0
        self.UseSlopedExtrapolation = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Boolean', self.UseServerCapabilitiesDefaults))
        body.append(pack_uatype('Boolean', self.TreatUncertainAsBad))
        body.append(pack_uatype('Byte', self.PercentDataBad))
        body.append(pack_uatype('Byte', self.PercentDataGood))
        body.append(pack_uatype('Boolean', self.UseSlopedExtrapolation))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AggregateConfiguration()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.UseServerCapabilitiesDefaults = unpack_uatype('Boolean', data)
        obj.TreatUncertainAsBad = unpack_uatype('Boolean', data)
        obj.PercentDataBad = unpack_uatype('Byte', data)
        obj.PercentDataGood = unpack_uatype('Byte', data)
        obj.UseSlopedExtrapolation = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'AggregateConfiguration(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'UseServerCapabilitiesDefaults:' + str(self.UseServerCapabilitiesDefaults) + ', '  + \
             'TreatUncertainAsBad:' + str(self.TreatUncertainAsBad) + ', '  + \
             'PercentDataBad:' + str(self.PercentDataBad) + ', '  + \
             'PercentDataGood:' + str(self.PercentDataGood) + ', '  + \
             'UseSlopedExtrapolation:' + str(self.UseSlopedExtrapolation) + ')'
    
    __repr__ = __str__
    
class AggregateFilter(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AggregateFilter_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StartTime = DateTime()
        self.AggregateType = NodeId()
        self.ProcessingInterval = 0
        self.AggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StartTime.to_binary())
        body.append(self.AggregateType.to_binary())
        body.append(pack_uatype('Double', self.ProcessingInterval))
        body.append(self.AggregateConfiguration.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AggregateFilter()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StartTime = DateTime.from_binary(data)
        obj.AggregateType = NodeId.from_binary(data)
        obj.ProcessingInterval = unpack_uatype('Double', data)
        obj.AggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AggregateFilter(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'AggregateType:' + str(self.AggregateType) + ', '  + \
             'ProcessingInterval:' + str(self.ProcessingInterval) + ', '  + \
             'AggregateConfiguration:' + str(self.AggregateConfiguration) + ')'
    
    __repr__ = __str__
    
class MonitoringFilterResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoringFilterResult_Encoding_DefaultBinary)
        self.Encoding = 0
        self.Body = b''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Body: 
            packet.append(pack_uatype('ByteString', self.Body))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoringFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Body = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'MonitoringFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class EventFilterResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EventFilterResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SelectClauseResults = []
        self.SelectClauseDiagnosticInfos = []
        self.WhereClauseResult = ContentFilterResult()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.SelectClauseResults)))
        for fieldname in self.SelectClauseResults:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.SelectClauseDiagnosticInfos)))
        for fieldname in self.SelectClauseDiagnosticInfos:
            body.append(fieldname.to_binary())
        body.append(self.WhereClauseResult.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.SelectClauseResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.SelectClauseDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        obj.WhereClauseResult = ContentFilterResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EventFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SelectClauseResults:' + str(self.SelectClauseResults) + ', '  + \
             'SelectClauseDiagnosticInfos:' + str(self.SelectClauseDiagnosticInfos) + ', '  + \
             'WhereClauseResult:' + str(self.WhereClauseResult) + ')'
    
    __repr__ = __str__
    
class AggregateFilterResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AggregateFilterResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.RevisedStartTime = DateTime()
        self.RevisedProcessingInterval = 0
        self.RevisedAggregateConfiguration = AggregateConfiguration()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.RevisedStartTime.to_binary())
        body.append(pack_uatype('Double', self.RevisedProcessingInterval))
        body.append(self.RevisedAggregateConfiguration.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AggregateFilterResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.RevisedStartTime = DateTime.from_binary(data)
        obj.RevisedProcessingInterval = unpack_uatype('Double', data)
        obj.RevisedAggregateConfiguration = AggregateConfiguration.from_binary(data)
        return obj
    
    def __str__(self):
        return 'AggregateFilterResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'RevisedStartTime:' + str(self.RevisedStartTime) + ', '  + \
             'RevisedProcessingInterval:' + str(self.RevisedProcessingInterval) + ', '  + \
             'RevisedAggregateConfiguration:' + str(self.RevisedAggregateConfiguration) + ')'
    
    __repr__ = __str__
    
class MonitoringParameters(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoringParameters_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ClientHandle = 0
        self.SamplingInterval = 0
        self.Filter = ExtensionObject()
        self.QueueSize = 0
        self.DiscardOldest = True
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.ClientHandle))
        body.append(pack_uatype('Double', self.SamplingInterval))
        body.append(self.Filter.to_binary())
        body.append(pack_uatype('UInt32', self.QueueSize))
        body.append(pack_uatype('Boolean', self.DiscardOldest))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoringParameters()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ClientHandle = unpack_uatype('UInt32', data)
        obj.SamplingInterval = unpack_uatype('Double', data)
        obj.Filter = ExtensionObject.from_binary(data)
        obj.QueueSize = unpack_uatype('UInt32', data)
        obj.DiscardOldest = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'MonitoringParameters(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ClientHandle:' + str(self.ClientHandle) + ', '  + \
             'SamplingInterval:' + str(self.SamplingInterval) + ', '  + \
             'Filter:' + str(self.Filter) + ', '  + \
             'QueueSize:' + str(self.QueueSize) + ', '  + \
             'DiscardOldest:' + str(self.DiscardOldest) + ')'
    
    __repr__ = __str__
    
class MonitoredItemCreateParameters(object):
    '''
    
    '''
    def __init__(self):
        self.MonitoringMode = 0
        self.RequestedParameters = MonitoringParameters()
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.MonitoringMode))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateParameters()
        obj.MonitoringMode = unpack_uatype('UInt32', data)
        obj.RequestedParameters = MonitoringParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemCreateParameters(' + 'MonitoringMode:' + str(self.MonitoringMode) + ', '  + \
             'RequestedParameters:' + str(self.RequestedParameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemCreateRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoredItemCreateRequest_Encoding_DefaultBinary)
        self.ItemToMonitor = ReadValueId()
        self.Parameters = MonitoredItemCreateParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ItemToMonitor.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.ItemToMonitor = ReadValueId.from_binary(data)
        obj.Parameters = MonitoredItemCreateParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemCreateRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ItemToMonitor:' + str(self.ItemToMonitor) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemCreateResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoredItemCreateResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.MonitoredItemId = 0
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(pack_uatype('UInt32', self.MonitoredItemId))
        body.append(pack_uatype('Double', self.RevisedSamplingInterval))
        body.append(pack_uatype('UInt32', self.RevisedQueueSize))
        body.append(self.FilterResult.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemCreateResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.MonitoredItemId = unpack_uatype('UInt32', data)
        obj.RevisedSamplingInterval = unpack_uatype('Double', data)
        obj.RevisedQueueSize = unpack_uatype('UInt32', data)
        obj.FilterResult = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemCreateResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'MonitoredItemId:' + str(self.MonitoredItemId) + ', '  + \
             'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', '  + \
             'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', '  + \
             'FilterResult:' + str(self.FilterResult) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToCreate = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.ItemsToCreate)))
        for fieldname in self.ItemsToCreate:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ItemsToCreate.append(MonitoredItemCreateRequest.from_binary(data))
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'ItemsToCreate:' + str(self.ItemsToCreate) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateMonitoredItemsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateMonitoredItemsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(MonitoredItemCreateResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class CreateMonitoredItemsResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateMonitoredItemsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateMonitoredItemsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemModifyRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoredItemModifyRequest_Encoding_DefaultBinary)
        self.MonitoredItemId = 0
        self.RequestedParameters = MonitoringParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt32', self.MonitoredItemId))
        packet.append(self.RequestedParameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemModifyRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.MonitoredItemId = unpack_uatype('UInt32', data)
        obj.RequestedParameters = MonitoringParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemModifyRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'MonitoredItemId:' + str(self.MonitoredItemId) + ', '  + \
             'RequestedParameters:' + str(self.RequestedParameters) + ')'
    
    __repr__ = __str__
    
class MonitoredItemModifyResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoredItemModifyResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.RevisedSamplingInterval = 0
        self.RevisedQueueSize = 0
        self.FilterResult = ExtensionObject()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(pack_uatype('Double', self.RevisedSamplingInterval))
        body.append(pack_uatype('UInt32', self.RevisedQueueSize))
        body.append(self.FilterResult.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemModifyResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.RevisedSamplingInterval = unpack_uatype('Double', data)
        obj.RevisedQueueSize = unpack_uatype('UInt32', data)
        obj.FilterResult = ExtensionObject.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemModifyResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'RevisedSamplingInterval:' + str(self.RevisedSamplingInterval) + ', '  + \
             'RevisedQueueSize:' + str(self.RevisedQueueSize) + ', '  + \
             'FilterResult:' + str(self.FilterResult) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.TimestampsToReturn = 0
        self.ItemsToModify = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.TimestampsToReturn))
        packet.append(struct.pack('<i', len(self.ItemsToModify)))
        for fieldname in self.ItemsToModify:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.TimestampsToReturn = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ItemsToModify.append(MonitoredItemModifyRequest.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'TimestampsToReturn:' + str(self.TimestampsToReturn) + ', '  + \
             'ItemsToModify:' + str(self.ItemsToModify) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifyMonitoredItemsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ModifyMonitoredItemsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(MonitoredItemModifyResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class ModifyMonitoredItemsResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifyMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifyMonitoredItemsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifyMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ModifyMonitoredItemsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifyMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoringMode = 0
        self.MonitoredItemIds = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.MonitoringMode))
        packet.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for fieldname in self.MonitoredItemIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.MonitoringMode = unpack_uatype('UInt32', data)
        obj.MonitoredItemIds = unpack_uatype_array('UInt32', data)
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'MonitoringMode:' + str(self.MonitoringMode) + ', '  + \
             'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetMonitoringModeParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetMonitoringModeParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class SetMonitoringModeResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetMonitoringModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetMonitoringModeResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetMonitoringModeResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetMonitoringModeResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetMonitoringModeResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetTriggeringParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.TriggeringItemId = 0
        self.LinksToAdd = []
        self.LinksToRemove = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.TriggeringItemId))
        packet.append(struct.pack('<i', len(self.LinksToAdd)))
        for fieldname in self.LinksToAdd:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(struct.pack('<i', len(self.LinksToRemove)))
        for fieldname in self.LinksToRemove:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetTriggeringParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.TriggeringItemId = unpack_uatype('UInt32', data)
        obj.LinksToAdd = unpack_uatype_array('UInt32', data)
        obj.LinksToRemove = unpack_uatype_array('UInt32', data)
        return obj
    
    def __str__(self):
        return 'SetTriggeringParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'TriggeringItemId:' + str(self.TriggeringItemId) + ', '  + \
             'LinksToAdd:' + str(self.LinksToAdd) + ', '  + \
             'LinksToRemove:' + str(self.LinksToRemove) + ')'
    
    __repr__ = __str__
    
class SetTriggeringRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetTriggeringParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetTriggeringRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetTriggeringParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetTriggeringRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetTriggeringResult(object):
    '''
    
    '''
    def __init__(self):
        self.AddResults = []
        self.AddDiagnosticInfos = []
        self.RemoveResults = []
        self.RemoveDiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.AddResults)))
        for fieldname in self.AddResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.AddDiagnosticInfos)))
        for fieldname in self.AddDiagnosticInfos:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.RemoveResults)))
        for fieldname in self.RemoveResults:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.RemoveDiagnosticInfos)))
        for fieldname in self.RemoveDiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetTriggeringResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.AddResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.AddDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.RemoveResults.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.RemoveDiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'SetTriggeringResult(' + 'AddResults:' + str(self.AddResults) + ', '  + \
             'AddDiagnosticInfos:' + str(self.AddDiagnosticInfos) + ', '  + \
             'RemoveResults:' + str(self.RemoveResults) + ', '  + \
             'RemoveDiagnosticInfos:' + str(self.RemoveDiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class SetTriggeringResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetTriggeringResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetTriggeringResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetTriggeringResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetTriggeringResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetTriggeringResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.MonitoredItemIds = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(struct.pack('<i', len(self.MonitoredItemIds)))
        for fieldname in self.MonitoredItemIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.MonitoredItemIds = unpack_uatype_array('UInt32', data)
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'MonitoredItemIds:' + str(self.MonitoredItemIds) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteMonitoredItemsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteMonitoredItemsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteMonitoredItemsResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteMonitoredItemsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteMonitoredItemsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteMonitoredItemsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteMonitoredItemsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteMonitoredItemsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionParameters(object):
    '''
    
    '''
    def __init__(self):
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = True
        self.Priority = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.RequestedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RequestedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RequestedMaxKeepAliveCount))
        packet.append(pack_uatype('UInt32', self.MaxNotificationsPerPublish))
        packet.append(pack_uatype('Boolean', self.PublishingEnabled))
        packet.append(pack_uatype('Byte', self.Priority))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionParameters()
        obj.RequestedPublishingInterval = unpack_uatype('Double', data)
        obj.RequestedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RequestedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        obj.MaxNotificationsPerPublish = unpack_uatype('UInt32', data)
        obj.PublishingEnabled = unpack_uatype('Boolean', data)
        obj.Priority = unpack_uatype('Byte', data)
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionParameters(' + 'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', '  + \
             'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', '  + \
             'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', '  + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', '  + \
             'PublishingEnabled:' + str(self.PublishingEnabled) + ', '  + \
             'Priority:' + str(self.Priority) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = CreateSubscriptionParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = CreateSubscriptionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionResult(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('Double', self.RevisedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RevisedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RevisedMaxKeepAliveCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionResult()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.RevisedPublishingInterval = unpack_uatype('Double', data)
        obj.RevisedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RevisedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', '  + \
             'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', '  + \
             'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'
    
    __repr__ = __str__
    
class CreateSubscriptionResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CreateSubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = CreateSubscriptionResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CreateSubscriptionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = CreateSubscriptionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CreateSubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.RequestedPublishingInterval = 0
        self.RequestedLifetimeCount = 0
        self.RequestedMaxKeepAliveCount = 0
        self.MaxNotificationsPerPublish = 0
        self.Priority = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('Double', self.RequestedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RequestedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RequestedMaxKeepAliveCount))
        packet.append(pack_uatype('UInt32', self.MaxNotificationsPerPublish))
        packet.append(pack_uatype('Byte', self.Priority))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.RequestedPublishingInterval = unpack_uatype('Double', data)
        obj.RequestedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RequestedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        obj.MaxNotificationsPerPublish = unpack_uatype('UInt32', data)
        obj.Priority = unpack_uatype('Byte', data)
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'RequestedPublishingInterval:' + str(self.RequestedPublishingInterval) + ', '  + \
             'RequestedLifetimeCount:' + str(self.RequestedLifetimeCount) + ', '  + \
             'RequestedMaxKeepAliveCount:' + str(self.RequestedMaxKeepAliveCount) + ', '  + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', '  + \
             'Priority:' + str(self.Priority) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = ModifySubscriptionParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = ModifySubscriptionParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionResult(object):
    '''
    
    '''
    def __init__(self):
        self.RevisedPublishingInterval = 0
        self.RevisedLifetimeCount = 0
        self.RevisedMaxKeepAliveCount = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Double', self.RevisedPublishingInterval))
        packet.append(pack_uatype('UInt32', self.RevisedLifetimeCount))
        packet.append(pack_uatype('UInt32', self.RevisedMaxKeepAliveCount))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionResult()
        obj.RevisedPublishingInterval = unpack_uatype('Double', data)
        obj.RevisedLifetimeCount = unpack_uatype('UInt32', data)
        obj.RevisedMaxKeepAliveCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionResult(' + 'RevisedPublishingInterval:' + str(self.RevisedPublishingInterval) + ', '  + \
             'RevisedLifetimeCount:' + str(self.RevisedLifetimeCount) + ', '  + \
             'RevisedMaxKeepAliveCount:' + str(self.RevisedMaxKeepAliveCount) + ')'
    
    __repr__ = __str__
    
class ModifySubscriptionResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModifySubscriptionResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = ModifySubscriptionResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModifySubscriptionResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = ModifySubscriptionResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ModifySubscriptionResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeParameters(object):
    '''
    
    '''
    def __init__(self):
        self.PublishingEnabled = True
        self.SubscriptionIds = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('Boolean', self.PublishingEnabled))
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeParameters()
        obj.PublishingEnabled = unpack_uatype('Boolean', data)
        obj.SubscriptionIds = unpack_uatype_array('UInt32', data)
        return obj
    
    def __str__(self):
        return 'SetPublishingModeParameters(' + 'PublishingEnabled:' + str(self.PublishingEnabled) + ', '  + \
             'SubscriptionIds:' + str(self.SubscriptionIds) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = SetPublishingModeParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = SetPublishingModeParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetPublishingModeRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'SetPublishingModeResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class SetPublishingModeResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SetPublishingModeResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = SetPublishingModeResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SetPublishingModeResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = SetPublishingModeResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SetPublishingModeResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class NotificationMessage(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.NotificationMessage_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SequenceNumber = 0
        self.PublishTime = DateTime()
        self.NotificationData = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SequenceNumber))
        body.append(self.PublishTime.to_binary())
        body.append(struct.pack('<i', len(self.NotificationData)))
        for fieldname in self.NotificationData:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NotificationMessage()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SequenceNumber = unpack_uatype('UInt32', data)
        obj.PublishTime = DateTime.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NotificationData.append(ExtensionObject.from_binary(data))
        return obj
    
    def __str__(self):
        return 'NotificationMessage(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SequenceNumber:' + str(self.SequenceNumber) + ', '  + \
             'PublishTime:' + str(self.PublishTime) + ', '  + \
             'NotificationData:' + str(self.NotificationData) + ')'
    
    __repr__ = __str__
    
class NotificationData(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.NotificationData_Encoding_DefaultBinary)
        self.Encoding = 0
        self.Body = b''
    
    def to_binary(self):
        packet = []
        if self.Body: self.Encoding |= (1 << 0)
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        if self.Body: 
            packet.append(pack_uatype('ByteString', self.Body))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NotificationData()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        if obj.Encoding & (1 << 0):
            obj.Body = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'NotificationData(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'Body:' + str(self.Body) + ')'
    
    __repr__ = __str__
    
class DataChangeNotification(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DataChangeNotification_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.MonitoredItems = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.MonitoredItems)))
        for fieldname in self.MonitoredItems:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DataChangeNotification()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.MonitoredItems.append(MonitoredItemNotification.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DataChangeNotification(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'MonitoredItems:' + str(self.MonitoredItems) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class MonitoredItemNotification(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.MonitoredItemNotification_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ClientHandle = 0
        self.Value = DataValue()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.ClientHandle))
        body.append(self.Value.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = MonitoredItemNotification()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ClientHandle = unpack_uatype('UInt32', data)
        obj.Value = DataValue.from_binary(data)
        return obj
    
    def __str__(self):
        return 'MonitoredItemNotification(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ClientHandle:' + str(self.ClientHandle) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class EventNotificationList(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EventNotificationList_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Events = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.Events)))
        for fieldname in self.Events:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventNotificationList()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Events.append(EventFieldList.from_binary(data))
        return obj
    
    def __str__(self):
        return 'EventNotificationList(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Events:' + str(self.Events) + ')'
    
    __repr__ = __str__
    
class EventFieldList(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EventFieldList_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ClientHandle = 0
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.ClientHandle))
        body.append(struct.pack('<i', len(self.EventFields)))
        for fieldname in self.EventFields:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EventFieldList()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ClientHandle = unpack_uatype('UInt32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.EventFields.append(Variant.from_binary(data))
        return obj
    
    def __str__(self):
        return 'EventFieldList(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ClientHandle:' + str(self.ClientHandle) + ', '  + \
             'EventFields:' + str(self.EventFields) + ')'
    
    __repr__ = __str__
    
class HistoryEventFieldList(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.HistoryEventFieldList_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.EventFields = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.EventFields)))
        for fieldname in self.EventFields:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = HistoryEventFieldList()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.EventFields.append(Variant.from_binary(data))
        return obj
    
    def __str__(self):
        return 'HistoryEventFieldList(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'EventFields:' + str(self.EventFields) + ')'
    
    __repr__ = __str__
    
class StatusChangeNotification(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.StatusChangeNotification_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Status = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.Status.to_binary())
        body.append(self.DiagnosticInfo.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = StatusChangeNotification()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Status = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'StatusChangeNotification(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Status:' + str(self.Status) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'
    
    __repr__ = __str__
    
class SubscriptionAcknowledgement(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SubscriptionAcknowledgement_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SubscriptionId = 0
        self.SequenceNumber = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.SubscriptionId))
        body.append(pack_uatype('UInt32', self.SequenceNumber))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SubscriptionAcknowledgement()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.SequenceNumber = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'SubscriptionAcknowledgement(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'SequenceNumber:' + str(self.SequenceNumber) + ')'
    
    __repr__ = __str__
    
class PublishParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionAcknowledgements = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionAcknowledgements)))
        for fieldname in self.SubscriptionAcknowledgements:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = PublishParameters()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.SubscriptionAcknowledgements.append(SubscriptionAcknowledgement.from_binary(data))
        return obj
    
    def __str__(self):
        return 'PublishParameters(' + 'SubscriptionAcknowledgements:' + str(self.SubscriptionAcknowledgements) + ')'
    
    __repr__ = __str__
    
class PublishRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.PublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = PublishParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = PublishRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = PublishParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'PublishRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class PublishResult(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.AvailableSequenceNumbers = []
        self.MoreNotifications = True
        self.NotificationMessage = NotificationMessage()
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for fieldname in self.AvailableSequenceNumbers:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(pack_uatype('Boolean', self.MoreNotifications))
        packet.append(self.NotificationMessage.to_binary())
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = PublishResult()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.AvailableSequenceNumbers = unpack_uatype_array('UInt32', data)
        obj.MoreNotifications = unpack_uatype('Boolean', data)
        obj.NotificationMessage = NotificationMessage.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'PublishResult(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ', '  + \
             'MoreNotifications:' + str(self.MoreNotifications) + ', '  + \
             'NotificationMessage:' + str(self.NotificationMessage) + ', '  + \
             'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class PublishResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.PublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = PublishResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = PublishResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = PublishResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'PublishResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RepublishParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionId = 0
        self.RetransmitSequenceNumber = 0
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.SubscriptionId))
        packet.append(pack_uatype('UInt32', self.RetransmitSequenceNumber))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishParameters()
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.RetransmitSequenceNumber = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'RepublishParameters(' + 'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'RetransmitSequenceNumber:' + str(self.RetransmitSequenceNumber) + ')'
    
    __repr__ = __str__
    
class RepublishRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RepublishRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = RepublishParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = RepublishParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RepublishRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class RepublishResult(object):
    '''
    
    '''
    def __init__(self):
        self.NotificationMessage = NotificationMessage()
    
    def to_binary(self):
        packet = []
        packet.append(self.NotificationMessage.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishResult()
        obj.NotificationMessage = NotificationMessage.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RepublishResult(' + 'NotificationMessage:' + str(self.NotificationMessage) + ')'
    
    __repr__ = __str__
    
class RepublishResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RepublishResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = RepublishResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RepublishResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = RepublishResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'RepublishResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TransferResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.AvailableSequenceNumbers = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(struct.pack('<i', len(self.AvailableSequenceNumbers)))
        for fieldname in self.AvailableSequenceNumbers:
            body.append(pack_uatype('UInt32', fieldname))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.AvailableSequenceNumbers = unpack_uatype_array('UInt32', data)
        return obj
    
    def __str__(self):
        return 'TransferResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'AvailableSequenceNumbers:' + str(self.AvailableSequenceNumbers) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionIds = []
        self.SendInitialValues = True
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(pack_uatype('UInt32', fieldname))
        packet.append(pack_uatype('Boolean', self.SendInitialValues))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsParameters()
        obj.SubscriptionIds = unpack_uatype_array('UInt32', data)
        obj.SendInitialValues = unpack_uatype('Boolean', data)
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ', '  + \
             'SendInitialValues:' + str(self.SendInitialValues) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TransferSubscriptionsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TransferSubscriptionsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(TransferResult.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class TransferSubscriptionsResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TransferSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TransferSubscriptionsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TransferSubscriptionsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TransferSubscriptionsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TransferSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsParameters(object):
    '''
    
    '''
    def __init__(self):
        self.SubscriptionIds = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.SubscriptionIds)))
        for fieldname in self.SubscriptionIds:
            packet.append(pack_uatype('UInt32', fieldname))
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsParameters()
        obj.SubscriptionIds = unpack_uatype_array('UInt32', data)
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsParameters(' + 'SubscriptionIds:' + str(self.SubscriptionIds) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = DeleteSubscriptionsParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = DeleteSubscriptionsParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsResult(object):
    '''
    
    '''
    def __init__(self):
        self.Results = []
        self.DiagnosticInfos = []
    
    def to_binary(self):
        packet = []
        packet.append(struct.pack('<i', len(self.Results)))
        for fieldname in self.Results:
            packet.append(fieldname.to_binary())
        packet.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            packet.append(fieldname.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsResult()
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Results.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsResult(' + 'Results:' + str(self.Results) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ')'
    
    __repr__ = __str__
    
class DeleteSubscriptionsResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DeleteSubscriptionsResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = DeleteSubscriptionsResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DeleteSubscriptionsResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = DeleteSubscriptionsResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'DeleteSubscriptionsResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class ScalarTestType(object):
    '''
    A complex type containing all possible scalar types used for testing.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ScalarTestType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Boolean = True
        self.SByte = SByte()
        self.Byte = 0
        self.Int16 = 0
        self.UInt16 = 0
        self.Int32 = 0
        self.UInt32 = 0
        self.Int64 = 0
        self.UInt64 = 0
        self.Float = 0
        self.Double = 0
        self.String = ''
        self.DateTime = DateTime()
        self.Guid = Guid()
        self.ByteString = b''
        self.XmlElement = XmlElement()
        self.NodeId = NodeId()
        self.ExpandedNodeId = ExpandedNodeId()
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
        self.QualifiedName = QualifiedName()
        self.LocalizedText = LocalizedText()
        self.ExtensionObject = ExtensionObject()
        self.DataValue = DataValue()
        self.EnumeratedValue = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Boolean', self.Boolean))
        body.append(pack_uatype('SByte', self.SByte))
        body.append(pack_uatype('Byte', self.Byte))
        body.append(pack_uatype('Int16', self.Int16))
        body.append(pack_uatype('UInt16', self.UInt16))
        body.append(pack_uatype('Int32', self.Int32))
        body.append(pack_uatype('UInt32', self.UInt32))
        body.append(pack_uatype('Int64', self.Int64))
        body.append(pack_uatype('UInt64', self.UInt64))
        body.append(pack_uatype('Float', self.Float))
        body.append(pack_uatype('Double', self.Double))
        body.append(pack_uatype('String', self.String))
        body.append(self.DateTime.to_binary())
        body.append(self.Guid.to_binary())
        body.append(pack_uatype('ByteString', self.ByteString))
        body.append(self.XmlElement.to_binary())
        body.append(self.NodeId.to_binary())
        body.append(self.ExpandedNodeId.to_binary())
        body.append(self.StatusCode.to_binary())
        body.append(self.DiagnosticInfo.to_binary())
        body.append(self.QualifiedName.to_binary())
        body.append(self.LocalizedText.to_binary())
        body.append(self.ExtensionObject.to_binary())
        body.append(self.DataValue.to_binary())
        body.append(pack_uatype('UInt32', self.EnumeratedValue))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ScalarTestType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Boolean = unpack_uatype('Boolean', data)
        obj.SByte = unpack_uatype('SByte', data)
        obj.Byte = unpack_uatype('Byte', data)
        obj.Int16 = unpack_uatype('Int16', data)
        obj.UInt16 = unpack_uatype('UInt16', data)
        obj.Int32 = unpack_uatype('Int32', data)
        obj.UInt32 = unpack_uatype('UInt32', data)
        obj.Int64 = unpack_uatype('Int64', data)
        obj.UInt64 = unpack_uatype('UInt64', data)
        obj.Float = unpack_uatype('Float', data)
        obj.Double = unpack_uatype('Double', data)
        obj.String = unpack_uatype('String', data)
        obj.DateTime = DateTime.from_binary(data)
        obj.Guid = Guid.from_binary(data)
        obj.ByteString = unpack_uatype('ByteString', data)
        obj.XmlElement = XmlElement.from_binary(data)
        obj.NodeId = NodeId.from_binary(data)
        obj.ExpandedNodeId = ExpandedNodeId.from_binary(data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        obj.QualifiedName = QualifiedName.from_binary(data)
        obj.LocalizedText = LocalizedText.from_binary(data)
        obj.ExtensionObject = ExtensionObject.from_binary(data)
        obj.DataValue = DataValue.from_binary(data)
        obj.EnumeratedValue = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ScalarTestType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Boolean:' + str(self.Boolean) + ', '  + \
             'SByte:' + str(self.SByte) + ', '  + \
             'Byte:' + str(self.Byte) + ', '  + \
             'Int16:' + str(self.Int16) + ', '  + \
             'UInt16:' + str(self.UInt16) + ', '  + \
             'Int32:' + str(self.Int32) + ', '  + \
             'UInt32:' + str(self.UInt32) + ', '  + \
             'Int64:' + str(self.Int64) + ', '  + \
             'UInt64:' + str(self.UInt64) + ', '  + \
             'Float:' + str(self.Float) + ', '  + \
             'Double:' + str(self.Double) + ', '  + \
             'String:' + str(self.String) + ', '  + \
             'DateTime:' + str(self.DateTime) + ', '  + \
             'Guid:' + str(self.Guid) + ', '  + \
             'ByteString:' + str(self.ByteString) + ', '  + \
             'XmlElement:' + str(self.XmlElement) + ', '  + \
             'NodeId:' + str(self.NodeId) + ', '  + \
             'ExpandedNodeId:' + str(self.ExpandedNodeId) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ', '  + \
             'QualifiedName:' + str(self.QualifiedName) + ', '  + \
             'LocalizedText:' + str(self.LocalizedText) + ', '  + \
             'ExtensionObject:' + str(self.ExtensionObject) + ', '  + \
             'DataValue:' + str(self.DataValue) + ', '  + \
             'EnumeratedValue:' + str(self.EnumeratedValue) + ')'
    
    __repr__ = __str__
    
class ArrayTestType(object):
    '''
    A complex type containing all possible array types used for testing.
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ArrayTestType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Booleans = []
        self.SBytes = []
        self.Int16s = []
        self.UInt16s = []
        self.Int32s = []
        self.UInt32s = []
        self.Int64s = []
        self.UInt64s = []
        self.Floats = []
        self.Doubles = []
        self.Strings = []
        self.DateTimes = []
        self.Guids = []
        self.ByteStrings = []
        self.XmlElements = []
        self.NodeIds = []
        self.ExpandedNodeIds = []
        self.StatusCodes = []
        self.DiagnosticInfos = []
        self.QualifiedNames = []
        self.LocalizedTexts = []
        self.ExtensionObjects = []
        self.DataValues = []
        self.Variants = []
        self.EnumeratedValues = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.Booleans)))
        for fieldname in self.Booleans:
            body.append(pack_uatype('Boolean', fieldname))
        body.append(struct.pack('<i', len(self.SBytes)))
        for fieldname in self.SBytes:
            body.append(pack_uatype('SByte', fieldname))
        body.append(struct.pack('<i', len(self.Int16s)))
        for fieldname in self.Int16s:
            body.append(pack_uatype('Int16', fieldname))
        body.append(struct.pack('<i', len(self.UInt16s)))
        for fieldname in self.UInt16s:
            body.append(pack_uatype('UInt16', fieldname))
        body.append(struct.pack('<i', len(self.Int32s)))
        for fieldname in self.Int32s:
            body.append(pack_uatype('Int32', fieldname))
        body.append(struct.pack('<i', len(self.UInt32s)))
        for fieldname in self.UInt32s:
            body.append(pack_uatype('UInt32', fieldname))
        body.append(struct.pack('<i', len(self.Int64s)))
        for fieldname in self.Int64s:
            body.append(pack_uatype('Int64', fieldname))
        body.append(struct.pack('<i', len(self.UInt64s)))
        for fieldname in self.UInt64s:
            body.append(pack_uatype('UInt64', fieldname))
        body.append(struct.pack('<i', len(self.Floats)))
        for fieldname in self.Floats:
            body.append(pack_uatype('Float', fieldname))
        body.append(struct.pack('<i', len(self.Doubles)))
        for fieldname in self.Doubles:
            body.append(pack_uatype('Double', fieldname))
        body.append(struct.pack('<i', len(self.Strings)))
        for fieldname in self.Strings:
            body.append(pack_uatype('String', fieldname))
        body.append(struct.pack('<i', len(self.DateTimes)))
        for fieldname in self.DateTimes:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.Guids)))
        for fieldname in self.Guids:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.ByteStrings)))
        for fieldname in self.ByteStrings:
            body.append(pack_uatype('ByteString', fieldname))
        body.append(struct.pack('<i', len(self.XmlElements)))
        for fieldname in self.XmlElements:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.NodeIds)))
        for fieldname in self.NodeIds:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.ExpandedNodeIds)))
        for fieldname in self.ExpandedNodeIds:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.StatusCodes)))
        for fieldname in self.StatusCodes:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.DiagnosticInfos)))
        for fieldname in self.DiagnosticInfos:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.QualifiedNames)))
        for fieldname in self.QualifiedNames:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.LocalizedTexts)))
        for fieldname in self.LocalizedTexts:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.ExtensionObjects)))
        for fieldname in self.ExtensionObjects:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.DataValues)))
        for fieldname in self.DataValues:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.Variants)))
        for fieldname in self.Variants:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.EnumeratedValues)))
        for fieldname in self.EnumeratedValues:
            body.append(pack_uatype('UInt32', fieldname))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ArrayTestType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Booleans = unpack_uatype_array('Boolean', data)
        obj.SBytes = unpack_uatype_array('SByte', data)
        obj.Int16s = unpack_uatype_array('Int16', data)
        obj.UInt16s = unpack_uatype_array('UInt16', data)
        obj.Int32s = unpack_uatype_array('Int32', data)
        obj.UInt32s = unpack_uatype_array('UInt32', data)
        obj.Int64s = unpack_uatype_array('Int64', data)
        obj.UInt64s = unpack_uatype_array('UInt64', data)
        obj.Floats = unpack_uatype_array('Float', data)
        obj.Doubles = unpack_uatype_array('Double', data)
        obj.Strings = unpack_uatype_array('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DateTimes.append(DateTime.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Guids.append(Guid.from_binary(data))
        obj.ByteStrings = unpack_uatype_array('ByteString', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.XmlElements.append(XmlElement.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NodeIds.append(NodeId.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ExpandedNodeIds.append(ExpandedNodeId.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.StatusCodes.append(StatusCode.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DiagnosticInfos.append(DiagnosticInfo.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.QualifiedNames.append(QualifiedName.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.LocalizedTexts.append(LocalizedText.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.ExtensionObjects.append(ExtensionObject.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.DataValues.append(DataValue.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.Variants.append(Variant.from_binary(data))
        obj.EnumeratedValues = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ArrayTestType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Booleans:' + str(self.Booleans) + ', '  + \
             'SBytes:' + str(self.SBytes) + ', '  + \
             'Int16s:' + str(self.Int16s) + ', '  + \
             'UInt16s:' + str(self.UInt16s) + ', '  + \
             'Int32s:' + str(self.Int32s) + ', '  + \
             'UInt32s:' + str(self.UInt32s) + ', '  + \
             'Int64s:' + str(self.Int64s) + ', '  + \
             'UInt64s:' + str(self.UInt64s) + ', '  + \
             'Floats:' + str(self.Floats) + ', '  + \
             'Doubles:' + str(self.Doubles) + ', '  + \
             'Strings:' + str(self.Strings) + ', '  + \
             'DateTimes:' + str(self.DateTimes) + ', '  + \
             'Guids:' + str(self.Guids) + ', '  + \
             'ByteStrings:' + str(self.ByteStrings) + ', '  + \
             'XmlElements:' + str(self.XmlElements) + ', '  + \
             'NodeIds:' + str(self.NodeIds) + ', '  + \
             'ExpandedNodeIds:' + str(self.ExpandedNodeIds) + ', '  + \
             'StatusCodes:' + str(self.StatusCodes) + ', '  + \
             'DiagnosticInfos:' + str(self.DiagnosticInfos) + ', '  + \
             'QualifiedNames:' + str(self.QualifiedNames) + ', '  + \
             'LocalizedTexts:' + str(self.LocalizedTexts) + ', '  + \
             'ExtensionObjects:' + str(self.ExtensionObjects) + ', '  + \
             'DataValues:' + str(self.DataValues) + ', '  + \
             'Variants:' + str(self.Variants) + ', '  + \
             'EnumeratedValues:' + str(self.EnumeratedValues) + ')'
    
    __repr__ = __str__
    
class CompositeTestType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.CompositeTestType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Field1 = ScalarTestType()
        self.Field2 = ArrayTestType()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.Field1.to_binary())
        body.append(self.Field2.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = CompositeTestType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Field1 = ScalarTestType.from_binary(data)
        obj.Field2 = ArrayTestType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'CompositeTestType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Field1:' + str(self.Field1) + ', '  + \
             'Field2:' + str(self.Field2) + ')'
    
    __repr__ = __str__
    
class TestStackParameters(object):
    '''
    
    '''
    def __init__(self):
        self.TestId = 0
        self.Iteration = 0
        self.Input = Variant()
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.TestId))
        packet.append(pack_uatype('Int32', self.Iteration))
        packet.append(self.Input.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackParameters()
        obj.TestId = unpack_uatype('UInt32', data)
        obj.Iteration = unpack_uatype('Int32', data)
        obj.Input = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackParameters(' + 'TestId:' + str(self.TestId) + ', '  + \
             'Iteration:' + str(self.Iteration) + ', '  + \
             'Input:' + str(self.Input) + ')'
    
    __repr__ = __str__
    
class TestStackRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TestStackRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TestStackParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TestStackParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TestStackResult(object):
    '''
    
    '''
    def __init__(self):
        self.Output = Variant()
    
    def to_binary(self):
        packet = []
        packet.append(self.Output.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackResult()
        obj.Output = Variant.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackResult(' + 'Output:' + str(self.Output) + ')'
    
    __repr__ = __str__
    
class TestStackResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TestStackResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TestStackResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TestStackResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TestStackExParameters(object):
    '''
    
    '''
    def __init__(self):
        self.TestId = 0
        self.Iteration = 0
        self.Input = CompositeTestType()
    
    def to_binary(self):
        packet = []
        packet.append(pack_uatype('UInt32', self.TestId))
        packet.append(pack_uatype('Int32', self.Iteration))
        packet.append(self.Input.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExParameters()
        obj.TestId = unpack_uatype('UInt32', data)
        obj.Iteration = unpack_uatype('Int32', data)
        obj.Input = CompositeTestType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExParameters(' + 'TestId:' + str(self.TestId) + ', '  + \
             'Iteration:' + str(self.Iteration) + ', '  + \
             'Input:' + str(self.Input) + ')'
    
    __repr__ = __str__
    
class TestStackExRequest(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TestStackExRequest_Encoding_DefaultBinary)
        self.RequestHeader = RequestHeader()
        self.Parameters = TestStackExParameters()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.RequestHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExRequest()
        obj.TypeId = NodeId.from_binary(data)
        obj.RequestHeader = RequestHeader.from_binary(data)
        obj.Parameters = TestStackExParameters.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExRequest(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'RequestHeader:' + str(self.RequestHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class TestStackExResult(object):
    '''
    
    '''
    def __init__(self):
        self.Output = CompositeTestType()
    
    def to_binary(self):
        packet = []
        packet.append(self.Output.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExResult()
        obj.Output = CompositeTestType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExResult(' + 'Output:' + str(self.Output) + ')'
    
    __repr__ = __str__
    
class TestStackExResponse(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.TestStackExResponse_Encoding_DefaultBinary)
        self.ResponseHeader = ResponseHeader()
        self.Parameters = TestStackExResult()
    
    def to_binary(self):
        packet = []
        packet.append(self.TypeId.to_binary())
        packet.append(self.ResponseHeader.to_binary())
        packet.append(self.Parameters.to_binary())
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = TestStackExResponse()
        obj.TypeId = NodeId.from_binary(data)
        obj.ResponseHeader = ResponseHeader.from_binary(data)
        obj.Parameters = TestStackExResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'TestStackExResponse(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'ResponseHeader:' + str(self.ResponseHeader) + ', '  + \
             'Parameters:' + str(self.Parameters) + ')'
    
    __repr__ = __str__
    
class BuildInfo(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.BuildInfo_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ProductUri = ''
        self.ManufacturerName = ''
        self.ProductName = ''
        self.SoftwareVersion = ''
        self.BuildNumber = ''
        self.BuildDate = DateTime()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.ProductUri))
        body.append(pack_uatype('String', self.ManufacturerName))
        body.append(pack_uatype('String', self.ProductName))
        body.append(pack_uatype('String', self.SoftwareVersion))
        body.append(pack_uatype('String', self.BuildNumber))
        body.append(self.BuildDate.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = BuildInfo()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ProductUri = unpack_uatype('String', data)
        obj.ManufacturerName = unpack_uatype('String', data)
        obj.ProductName = unpack_uatype('String', data)
        obj.SoftwareVersion = unpack_uatype('String', data)
        obj.BuildNumber = unpack_uatype('String', data)
        obj.BuildDate = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'BuildInfo(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ProductUri:' + str(self.ProductUri) + ', '  + \
             'ManufacturerName:' + str(self.ManufacturerName) + ', '  + \
             'ProductName:' + str(self.ProductName) + ', '  + \
             'SoftwareVersion:' + str(self.SoftwareVersion) + ', '  + \
             'BuildNumber:' + str(self.BuildNumber) + ', '  + \
             'BuildDate:' + str(self.BuildDate) + ')'
    
    __repr__ = __str__
    
class RedundantServerDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.RedundantServerDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ServerId = ''
        self.ServiceLevel = 0
        self.ServerState = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.ServerId))
        body.append(pack_uatype('Byte', self.ServiceLevel))
        body.append(pack_uatype('UInt32', self.ServerState))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = RedundantServerDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ServerId = unpack_uatype('String', data)
        obj.ServiceLevel = unpack_uatype('Byte', data)
        obj.ServerState = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'RedundantServerDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ServerId:' + str(self.ServerId) + ', '  + \
             'ServiceLevel:' + str(self.ServiceLevel) + ', '  + \
             'ServerState:' + str(self.ServerState) + ')'
    
    __repr__ = __str__
    
class EndpointUrlListDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EndpointUrlListDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.EndpointUrlList = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(struct.pack('<i', len(self.EndpointUrlList)))
        for fieldname in self.EndpointUrlList:
            body.append(pack_uatype('String', fieldname))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EndpointUrlListDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.EndpointUrlList = unpack_uatype_array('String', data)
        return obj
    
    def __str__(self):
        return 'EndpointUrlListDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'EndpointUrlList:' + str(self.EndpointUrlList) + ')'
    
    __repr__ = __str__
    
class NetworkGroupDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.NetworkGroupDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ServerUri = ''
        self.NetworkPaths = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.ServerUri))
        body.append(struct.pack('<i', len(self.NetworkPaths)))
        for fieldname in self.NetworkPaths:
            body.append(fieldname.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = NetworkGroupDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ServerUri = unpack_uatype('String', data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.NetworkPaths.append(EndpointUrlListDataType.from_binary(data))
        return obj
    
    def __str__(self):
        return 'NetworkGroupDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ServerUri:' + str(self.ServerUri) + ', '  + \
             'NetworkPaths:' + str(self.NetworkPaths) + ')'
    
    __repr__ = __str__
    
class SamplingIntervalDiagnosticsDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SamplingIntervalDiagnosticsDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SamplingInterval = 0
        self.MonitoredItemCount = 0
        self.MaxMonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Double', self.SamplingInterval))
        body.append(pack_uatype('UInt32', self.MonitoredItemCount))
        body.append(pack_uatype('UInt32', self.MaxMonitoredItemCount))
        body.append(pack_uatype('UInt32', self.DisabledMonitoredItemCount))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SamplingIntervalDiagnosticsDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SamplingInterval = unpack_uatype('Double', data)
        obj.MonitoredItemCount = unpack_uatype('UInt32', data)
        obj.MaxMonitoredItemCount = unpack_uatype('UInt32', data)
        obj.DisabledMonitoredItemCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'SamplingIntervalDiagnosticsDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SamplingInterval:' + str(self.SamplingInterval) + ', '  + \
             'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', '  + \
             'MaxMonitoredItemCount:' + str(self.MaxMonitoredItemCount) + ', '  + \
             'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ')'
    
    __repr__ = __str__
    
class ServerDiagnosticsSummaryDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ServerDiagnosticsSummaryDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.ServerViewCount = 0
        self.CurrentSessionCount = 0
        self.CumulatedSessionCount = 0
        self.SecurityRejectedSessionCount = 0
        self.RejectedSessionCount = 0
        self.SessionTimeoutCount = 0
        self.SessionAbortCount = 0
        self.CurrentSubscriptionCount = 0
        self.CumulatedSubscriptionCount = 0
        self.PublishingIntervalCount = 0
        self.SecurityRejectedRequestsCount = 0
        self.RejectedRequestsCount = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.ServerViewCount))
        body.append(pack_uatype('UInt32', self.CurrentSessionCount))
        body.append(pack_uatype('UInt32', self.CumulatedSessionCount))
        body.append(pack_uatype('UInt32', self.SecurityRejectedSessionCount))
        body.append(pack_uatype('UInt32', self.RejectedSessionCount))
        body.append(pack_uatype('UInt32', self.SessionTimeoutCount))
        body.append(pack_uatype('UInt32', self.SessionAbortCount))
        body.append(pack_uatype('UInt32', self.CurrentSubscriptionCount))
        body.append(pack_uatype('UInt32', self.CumulatedSubscriptionCount))
        body.append(pack_uatype('UInt32', self.PublishingIntervalCount))
        body.append(pack_uatype('UInt32', self.SecurityRejectedRequestsCount))
        body.append(pack_uatype('UInt32', self.RejectedRequestsCount))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServerDiagnosticsSummaryDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.ServerViewCount = unpack_uatype('UInt32', data)
        obj.CurrentSessionCount = unpack_uatype('UInt32', data)
        obj.CumulatedSessionCount = unpack_uatype('UInt32', data)
        obj.SecurityRejectedSessionCount = unpack_uatype('UInt32', data)
        obj.RejectedSessionCount = unpack_uatype('UInt32', data)
        obj.SessionTimeoutCount = unpack_uatype('UInt32', data)
        obj.SessionAbortCount = unpack_uatype('UInt32', data)
        obj.CurrentSubscriptionCount = unpack_uatype('UInt32', data)
        obj.CumulatedSubscriptionCount = unpack_uatype('UInt32', data)
        obj.PublishingIntervalCount = unpack_uatype('UInt32', data)
        obj.SecurityRejectedRequestsCount = unpack_uatype('UInt32', data)
        obj.RejectedRequestsCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ServerDiagnosticsSummaryDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'ServerViewCount:' + str(self.ServerViewCount) + ', '  + \
             'CurrentSessionCount:' + str(self.CurrentSessionCount) + ', '  + \
             'CumulatedSessionCount:' + str(self.CumulatedSessionCount) + ', '  + \
             'SecurityRejectedSessionCount:' + str(self.SecurityRejectedSessionCount) + ', '  + \
             'RejectedSessionCount:' + str(self.RejectedSessionCount) + ', '  + \
             'SessionTimeoutCount:' + str(self.SessionTimeoutCount) + ', '  + \
             'SessionAbortCount:' + str(self.SessionAbortCount) + ', '  + \
             'CurrentSubscriptionCount:' + str(self.CurrentSubscriptionCount) + ', '  + \
             'CumulatedSubscriptionCount:' + str(self.CumulatedSubscriptionCount) + ', '  + \
             'PublishingIntervalCount:' + str(self.PublishingIntervalCount) + ', '  + \
             'SecurityRejectedRequestsCount:' + str(self.SecurityRejectedRequestsCount) + ', '  + \
             'RejectedRequestsCount:' + str(self.RejectedRequestsCount) + ')'
    
    __repr__ = __str__
    
class ServerStatusDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ServerStatusDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StartTime = DateTime()
        self.CurrentTime = DateTime()
        self.State = 0
        self.BuildInfo = BuildInfo()
        self.SecondsTillShutdown = 0
        self.ShutdownReason = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StartTime.to_binary())
        body.append(self.CurrentTime.to_binary())
        body.append(pack_uatype('UInt32', self.State))
        body.append(self.BuildInfo.to_binary())
        body.append(pack_uatype('UInt32', self.SecondsTillShutdown))
        body.append(self.ShutdownReason.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServerStatusDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StartTime = DateTime.from_binary(data)
        obj.CurrentTime = DateTime.from_binary(data)
        obj.State = unpack_uatype('UInt32', data)
        obj.BuildInfo = BuildInfo.from_binary(data)
        obj.SecondsTillShutdown = unpack_uatype('UInt32', data)
        obj.ShutdownReason = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ServerStatusDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StartTime:' + str(self.StartTime) + ', '  + \
             'CurrentTime:' + str(self.CurrentTime) + ', '  + \
             'State:' + str(self.State) + ', '  + \
             'BuildInfo:' + str(self.BuildInfo) + ', '  + \
             'SecondsTillShutdown:' + str(self.SecondsTillShutdown) + ', '  + \
             'ShutdownReason:' + str(self.ShutdownReason) + ')'
    
    __repr__ = __str__
    
class SessionDiagnosticsDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SessionDiagnosticsDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SessionId = NodeId()
        self.SessionName = ''
        self.ClientDescription = ApplicationDescription()
        self.ServerUri = ''
        self.EndpointUrl = ''
        self.LocaleIds = []
        self.ActualSessionTimeout = 0
        self.MaxResponseMessageSize = 0
        self.ClientConnectionTime = DateTime()
        self.ClientLastContactTime = DateTime()
        self.CurrentSubscriptionsCount = 0
        self.CurrentMonitoredItemsCount = 0
        self.CurrentPublishRequestsInQueue = 0
        self.TotalRequestCount = ServiceCounterDataType()
        self.UnauthorizedRequestCount = 0
        self.ReadCount = ServiceCounterDataType()
        self.HistoryReadCount = ServiceCounterDataType()
        self.WriteCount = ServiceCounterDataType()
        self.HistoryUpdateCount = ServiceCounterDataType()
        self.CallCount = ServiceCounterDataType()
        self.CreateMonitoredItemsCount = ServiceCounterDataType()
        self.ModifyMonitoredItemsCount = ServiceCounterDataType()
        self.SetMonitoringModeCount = ServiceCounterDataType()
        self.SetTriggeringCount = ServiceCounterDataType()
        self.DeleteMonitoredItemsCount = ServiceCounterDataType()
        self.CreateSubscriptionCount = ServiceCounterDataType()
        self.ModifySubscriptionCount = ServiceCounterDataType()
        self.SetPublishingModeCount = ServiceCounterDataType()
        self.PublishCount = ServiceCounterDataType()
        self.RepublishCount = ServiceCounterDataType()
        self.TransferSubscriptionsCount = ServiceCounterDataType()
        self.DeleteSubscriptionsCount = ServiceCounterDataType()
        self.AddNodesCount = ServiceCounterDataType()
        self.AddReferencesCount = ServiceCounterDataType()
        self.DeleteNodesCount = ServiceCounterDataType()
        self.DeleteReferencesCount = ServiceCounterDataType()
        self.BrowseCount = ServiceCounterDataType()
        self.BrowseNextCount = ServiceCounterDataType()
        self.TranslateBrowsePathsToNodeIdsCount = ServiceCounterDataType()
        self.QueryFirstCount = ServiceCounterDataType()
        self.QueryNextCount = ServiceCounterDataType()
        self.RegisterNodesCount = ServiceCounterDataType()
        self.UnregisterNodesCount = ServiceCounterDataType()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.SessionId.to_binary())
        body.append(pack_uatype('String', self.SessionName))
        body.append(self.ClientDescription.to_binary())
        body.append(pack_uatype('String', self.ServerUri))
        body.append(pack_uatype('String', self.EndpointUrl))
        body.append(struct.pack('<i', len(self.LocaleIds)))
        for fieldname in self.LocaleIds:
            body.append(pack_uatype('String', fieldname))
        body.append(pack_uatype('Double', self.ActualSessionTimeout))
        body.append(pack_uatype('UInt32', self.MaxResponseMessageSize))
        body.append(self.ClientConnectionTime.to_binary())
        body.append(self.ClientLastContactTime.to_binary())
        body.append(pack_uatype('UInt32', self.CurrentSubscriptionsCount))
        body.append(pack_uatype('UInt32', self.CurrentMonitoredItemsCount))
        body.append(pack_uatype('UInt32', self.CurrentPublishRequestsInQueue))
        body.append(self.TotalRequestCount.to_binary())
        body.append(pack_uatype('UInt32', self.UnauthorizedRequestCount))
        body.append(self.ReadCount.to_binary())
        body.append(self.HistoryReadCount.to_binary())
        body.append(self.WriteCount.to_binary())
        body.append(self.HistoryUpdateCount.to_binary())
        body.append(self.CallCount.to_binary())
        body.append(self.CreateMonitoredItemsCount.to_binary())
        body.append(self.ModifyMonitoredItemsCount.to_binary())
        body.append(self.SetMonitoringModeCount.to_binary())
        body.append(self.SetTriggeringCount.to_binary())
        body.append(self.DeleteMonitoredItemsCount.to_binary())
        body.append(self.CreateSubscriptionCount.to_binary())
        body.append(self.ModifySubscriptionCount.to_binary())
        body.append(self.SetPublishingModeCount.to_binary())
        body.append(self.PublishCount.to_binary())
        body.append(self.RepublishCount.to_binary())
        body.append(self.TransferSubscriptionsCount.to_binary())
        body.append(self.DeleteSubscriptionsCount.to_binary())
        body.append(self.AddNodesCount.to_binary())
        body.append(self.AddReferencesCount.to_binary())
        body.append(self.DeleteNodesCount.to_binary())
        body.append(self.DeleteReferencesCount.to_binary())
        body.append(self.BrowseCount.to_binary())
        body.append(self.BrowseNextCount.to_binary())
        body.append(self.TranslateBrowsePathsToNodeIdsCount.to_binary())
        body.append(self.QueryFirstCount.to_binary())
        body.append(self.QueryNextCount.to_binary())
        body.append(self.RegisterNodesCount.to_binary())
        body.append(self.UnregisterNodesCount.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SessionDiagnosticsDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SessionId = NodeId.from_binary(data)
        obj.SessionName = unpack_uatype('String', data)
        obj.ClientDescription = ApplicationDescription.from_binary(data)
        obj.ServerUri = unpack_uatype('String', data)
        obj.EndpointUrl = unpack_uatype('String', data)
        obj.LocaleIds = unpack_uatype_array('String', data)
        obj.ActualSessionTimeout = unpack_uatype('Double', data)
        obj.MaxResponseMessageSize = unpack_uatype('UInt32', data)
        obj.ClientConnectionTime = DateTime.from_binary(data)
        obj.ClientLastContactTime = DateTime.from_binary(data)
        obj.CurrentSubscriptionsCount = unpack_uatype('UInt32', data)
        obj.CurrentMonitoredItemsCount = unpack_uatype('UInt32', data)
        obj.CurrentPublishRequestsInQueue = unpack_uatype('UInt32', data)
        obj.TotalRequestCount = ServiceCounterDataType.from_binary(data)
        obj.UnauthorizedRequestCount = unpack_uatype('UInt32', data)
        obj.ReadCount = ServiceCounterDataType.from_binary(data)
        obj.HistoryReadCount = ServiceCounterDataType.from_binary(data)
        obj.WriteCount = ServiceCounterDataType.from_binary(data)
        obj.HistoryUpdateCount = ServiceCounterDataType.from_binary(data)
        obj.CallCount = ServiceCounterDataType.from_binary(data)
        obj.CreateMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        obj.ModifyMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        obj.SetMonitoringModeCount = ServiceCounterDataType.from_binary(data)
        obj.SetTriggeringCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteMonitoredItemsCount = ServiceCounterDataType.from_binary(data)
        obj.CreateSubscriptionCount = ServiceCounterDataType.from_binary(data)
        obj.ModifySubscriptionCount = ServiceCounterDataType.from_binary(data)
        obj.SetPublishingModeCount = ServiceCounterDataType.from_binary(data)
        obj.PublishCount = ServiceCounterDataType.from_binary(data)
        obj.RepublishCount = ServiceCounterDataType.from_binary(data)
        obj.TransferSubscriptionsCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteSubscriptionsCount = ServiceCounterDataType.from_binary(data)
        obj.AddNodesCount = ServiceCounterDataType.from_binary(data)
        obj.AddReferencesCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteNodesCount = ServiceCounterDataType.from_binary(data)
        obj.DeleteReferencesCount = ServiceCounterDataType.from_binary(data)
        obj.BrowseCount = ServiceCounterDataType.from_binary(data)
        obj.BrowseNextCount = ServiceCounterDataType.from_binary(data)
        obj.TranslateBrowsePathsToNodeIdsCount = ServiceCounterDataType.from_binary(data)
        obj.QueryFirstCount = ServiceCounterDataType.from_binary(data)
        obj.QueryNextCount = ServiceCounterDataType.from_binary(data)
        obj.RegisterNodesCount = ServiceCounterDataType.from_binary(data)
        obj.UnregisterNodesCount = ServiceCounterDataType.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SessionDiagnosticsDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SessionId:' + str(self.SessionId) + ', '  + \
             'SessionName:' + str(self.SessionName) + ', '  + \
             'ClientDescription:' + str(self.ClientDescription) + ', '  + \
             'ServerUri:' + str(self.ServerUri) + ', '  + \
             'EndpointUrl:' + str(self.EndpointUrl) + ', '  + \
             'LocaleIds:' + str(self.LocaleIds) + ', '  + \
             'ActualSessionTimeout:' + str(self.ActualSessionTimeout) + ', '  + \
             'MaxResponseMessageSize:' + str(self.MaxResponseMessageSize) + ', '  + \
             'ClientConnectionTime:' + str(self.ClientConnectionTime) + ', '  + \
             'ClientLastContactTime:' + str(self.ClientLastContactTime) + ', '  + \
             'CurrentSubscriptionsCount:' + str(self.CurrentSubscriptionsCount) + ', '  + \
             'CurrentMonitoredItemsCount:' + str(self.CurrentMonitoredItemsCount) + ', '  + \
             'CurrentPublishRequestsInQueue:' + str(self.CurrentPublishRequestsInQueue) + ', '  + \
             'TotalRequestCount:' + str(self.TotalRequestCount) + ', '  + \
             'UnauthorizedRequestCount:' + str(self.UnauthorizedRequestCount) + ', '  + \
             'ReadCount:' + str(self.ReadCount) + ', '  + \
             'HistoryReadCount:' + str(self.HistoryReadCount) + ', '  + \
             'WriteCount:' + str(self.WriteCount) + ', '  + \
             'HistoryUpdateCount:' + str(self.HistoryUpdateCount) + ', '  + \
             'CallCount:' + str(self.CallCount) + ', '  + \
             'CreateMonitoredItemsCount:' + str(self.CreateMonitoredItemsCount) + ', '  + \
             'ModifyMonitoredItemsCount:' + str(self.ModifyMonitoredItemsCount) + ', '  + \
             'SetMonitoringModeCount:' + str(self.SetMonitoringModeCount) + ', '  + \
             'SetTriggeringCount:' + str(self.SetTriggeringCount) + ', '  + \
             'DeleteMonitoredItemsCount:' + str(self.DeleteMonitoredItemsCount) + ', '  + \
             'CreateSubscriptionCount:' + str(self.CreateSubscriptionCount) + ', '  + \
             'ModifySubscriptionCount:' + str(self.ModifySubscriptionCount) + ', '  + \
             'SetPublishingModeCount:' + str(self.SetPublishingModeCount) + ', '  + \
             'PublishCount:' + str(self.PublishCount) + ', '  + \
             'RepublishCount:' + str(self.RepublishCount) + ', '  + \
             'TransferSubscriptionsCount:' + str(self.TransferSubscriptionsCount) + ', '  + \
             'DeleteSubscriptionsCount:' + str(self.DeleteSubscriptionsCount) + ', '  + \
             'AddNodesCount:' + str(self.AddNodesCount) + ', '  + \
             'AddReferencesCount:' + str(self.AddReferencesCount) + ', '  + \
             'DeleteNodesCount:' + str(self.DeleteNodesCount) + ', '  + \
             'DeleteReferencesCount:' + str(self.DeleteReferencesCount) + ', '  + \
             'BrowseCount:' + str(self.BrowseCount) + ', '  + \
             'BrowseNextCount:' + str(self.BrowseNextCount) + ', '  + \
             'TranslateBrowsePathsToNodeIdsCount:' + str(self.TranslateBrowsePathsToNodeIdsCount) + ', '  + \
             'QueryFirstCount:' + str(self.QueryFirstCount) + ', '  + \
             'QueryNextCount:' + str(self.QueryNextCount) + ', '  + \
             'RegisterNodesCount:' + str(self.RegisterNodesCount) + ', '  + \
             'UnregisterNodesCount:' + str(self.UnregisterNodesCount) + ')'
    
    __repr__ = __str__
    
class SessionSecurityDiagnosticsDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SessionSecurityDiagnosticsDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SessionId = NodeId()
        self.ClientUserIdOfSession = ''
        self.ClientUserIdHistory = []
        self.AuthenticationMechanism = ''
        self.TransportProtocol = ''
        self.SecurityMode = 0
        self.SecurityPolicyUri = ''
        self.ClientCertificate = b''
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.SessionId.to_binary())
        body.append(pack_uatype('String', self.ClientUserIdOfSession))
        body.append(struct.pack('<i', len(self.ClientUserIdHistory)))
        for fieldname in self.ClientUserIdHistory:
            body.append(pack_uatype('String', fieldname))
        body.append(pack_uatype('String', self.AuthenticationMechanism))
        body.append(pack_uatype('String', self.TransportProtocol))
        body.append(pack_uatype('UInt32', self.SecurityMode))
        body.append(pack_uatype('String', self.SecurityPolicyUri))
        body.append(pack_uatype('ByteString', self.ClientCertificate))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SessionSecurityDiagnosticsDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SessionId = NodeId.from_binary(data)
        obj.ClientUserIdOfSession = unpack_uatype('String', data)
        obj.ClientUserIdHistory = unpack_uatype_array('String', data)
        obj.AuthenticationMechanism = unpack_uatype('String', data)
        obj.TransportProtocol = unpack_uatype('String', data)
        obj.SecurityMode = unpack_uatype('UInt32', data)
        obj.SecurityPolicyUri = unpack_uatype('String', data)
        obj.ClientCertificate = unpack_uatype('ByteString', data)
        return obj
    
    def __str__(self):
        return 'SessionSecurityDiagnosticsDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SessionId:' + str(self.SessionId) + ', '  + \
             'ClientUserIdOfSession:' + str(self.ClientUserIdOfSession) + ', '  + \
             'ClientUserIdHistory:' + str(self.ClientUserIdHistory) + ', '  + \
             'AuthenticationMechanism:' + str(self.AuthenticationMechanism) + ', '  + \
             'TransportProtocol:' + str(self.TransportProtocol) + ', '  + \
             'SecurityMode:' + str(self.SecurityMode) + ', '  + \
             'SecurityPolicyUri:' + str(self.SecurityPolicyUri) + ', '  + \
             'ClientCertificate:' + str(self.ClientCertificate) + ')'
    
    __repr__ = __str__
    
class ServiceCounterDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ServiceCounterDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.TotalCount = 0
        self.ErrorCount = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('UInt32', self.TotalCount))
        body.append(pack_uatype('UInt32', self.ErrorCount))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ServiceCounterDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.TotalCount = unpack_uatype('UInt32', data)
        obj.ErrorCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'ServiceCounterDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'TotalCount:' + str(self.TotalCount) + ', '  + \
             'ErrorCount:' + str(self.ErrorCount) + ')'
    
    __repr__ = __str__
    
class StatusResult(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.StatusResult_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.StatusCode = StatusCode()
        self.DiagnosticInfo = DiagnosticInfo()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.StatusCode.to_binary())
        body.append(self.DiagnosticInfo.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = StatusResult()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.StatusCode = StatusCode.from_binary(data)
        obj.DiagnosticInfo = DiagnosticInfo.from_binary(data)
        return obj
    
    def __str__(self):
        return 'StatusResult(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'StatusCode:' + str(self.StatusCode) + ', '  + \
             'DiagnosticInfo:' + str(self.DiagnosticInfo) + ')'
    
    __repr__ = __str__
    
class SubscriptionDiagnosticsDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SubscriptionDiagnosticsDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.SessionId = NodeId()
        self.SubscriptionId = 0
        self.Priority = 0
        self.PublishingInterval = 0
        self.MaxKeepAliveCount = 0
        self.MaxLifetimeCount = 0
        self.MaxNotificationsPerPublish = 0
        self.PublishingEnabled = True
        self.ModifyCount = 0
        self.EnableCount = 0
        self.DisableCount = 0
        self.RepublishRequestCount = 0
        self.RepublishMessageRequestCount = 0
        self.RepublishMessageCount = 0
        self.TransferRequestCount = 0
        self.TransferredToAltClientCount = 0
        self.TransferredToSameClientCount = 0
        self.PublishRequestCount = 0
        self.DataChangeNotificationsCount = 0
        self.EventNotificationsCount = 0
        self.NotificationsCount = 0
        self.LatePublishRequestCount = 0
        self.CurrentKeepAliveCount = 0
        self.CurrentLifetimeCount = 0
        self.UnacknowledgedMessageCount = 0
        self.DiscardedMessageCount = 0
        self.MonitoredItemCount = 0
        self.DisabledMonitoredItemCount = 0
        self.MonitoringQueueOverflowCount = 0
        self.NextSequenceNumber = 0
        self.EventQueueOverFlowCount = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.SessionId.to_binary())
        body.append(pack_uatype('UInt32', self.SubscriptionId))
        body.append(pack_uatype('Byte', self.Priority))
        body.append(pack_uatype('Double', self.PublishingInterval))
        body.append(pack_uatype('UInt32', self.MaxKeepAliveCount))
        body.append(pack_uatype('UInt32', self.MaxLifetimeCount))
        body.append(pack_uatype('UInt32', self.MaxNotificationsPerPublish))
        body.append(pack_uatype('Boolean', self.PublishingEnabled))
        body.append(pack_uatype('UInt32', self.ModifyCount))
        body.append(pack_uatype('UInt32', self.EnableCount))
        body.append(pack_uatype('UInt32', self.DisableCount))
        body.append(pack_uatype('UInt32', self.RepublishRequestCount))
        body.append(pack_uatype('UInt32', self.RepublishMessageRequestCount))
        body.append(pack_uatype('UInt32', self.RepublishMessageCount))
        body.append(pack_uatype('UInt32', self.TransferRequestCount))
        body.append(pack_uatype('UInt32', self.TransferredToAltClientCount))
        body.append(pack_uatype('UInt32', self.TransferredToSameClientCount))
        body.append(pack_uatype('UInt32', self.PublishRequestCount))
        body.append(pack_uatype('UInt32', self.DataChangeNotificationsCount))
        body.append(pack_uatype('UInt32', self.EventNotificationsCount))
        body.append(pack_uatype('UInt32', self.NotificationsCount))
        body.append(pack_uatype('UInt32', self.LatePublishRequestCount))
        body.append(pack_uatype('UInt32', self.CurrentKeepAliveCount))
        body.append(pack_uatype('UInt32', self.CurrentLifetimeCount))
        body.append(pack_uatype('UInt32', self.UnacknowledgedMessageCount))
        body.append(pack_uatype('UInt32', self.DiscardedMessageCount))
        body.append(pack_uatype('UInt32', self.MonitoredItemCount))
        body.append(pack_uatype('UInt32', self.DisabledMonitoredItemCount))
        body.append(pack_uatype('UInt32', self.MonitoringQueueOverflowCount))
        body.append(pack_uatype('UInt32', self.NextSequenceNumber))
        body.append(pack_uatype('UInt32', self.EventQueueOverFlowCount))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SubscriptionDiagnosticsDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.SessionId = NodeId.from_binary(data)
        obj.SubscriptionId = unpack_uatype('UInt32', data)
        obj.Priority = unpack_uatype('Byte', data)
        obj.PublishingInterval = unpack_uatype('Double', data)
        obj.MaxKeepAliveCount = unpack_uatype('UInt32', data)
        obj.MaxLifetimeCount = unpack_uatype('UInt32', data)
        obj.MaxNotificationsPerPublish = unpack_uatype('UInt32', data)
        obj.PublishingEnabled = unpack_uatype('Boolean', data)
        obj.ModifyCount = unpack_uatype('UInt32', data)
        obj.EnableCount = unpack_uatype('UInt32', data)
        obj.DisableCount = unpack_uatype('UInt32', data)
        obj.RepublishRequestCount = unpack_uatype('UInt32', data)
        obj.RepublishMessageRequestCount = unpack_uatype('UInt32', data)
        obj.RepublishMessageCount = unpack_uatype('UInt32', data)
        obj.TransferRequestCount = unpack_uatype('UInt32', data)
        obj.TransferredToAltClientCount = unpack_uatype('UInt32', data)
        obj.TransferredToSameClientCount = unpack_uatype('UInt32', data)
        obj.PublishRequestCount = unpack_uatype('UInt32', data)
        obj.DataChangeNotificationsCount = unpack_uatype('UInt32', data)
        obj.EventNotificationsCount = unpack_uatype('UInt32', data)
        obj.NotificationsCount = unpack_uatype('UInt32', data)
        obj.LatePublishRequestCount = unpack_uatype('UInt32', data)
        obj.CurrentKeepAliveCount = unpack_uatype('UInt32', data)
        obj.CurrentLifetimeCount = unpack_uatype('UInt32', data)
        obj.UnacknowledgedMessageCount = unpack_uatype('UInt32', data)
        obj.DiscardedMessageCount = unpack_uatype('UInt32', data)
        obj.MonitoredItemCount = unpack_uatype('UInt32', data)
        obj.DisabledMonitoredItemCount = unpack_uatype('UInt32', data)
        obj.MonitoringQueueOverflowCount = unpack_uatype('UInt32', data)
        obj.NextSequenceNumber = unpack_uatype('UInt32', data)
        obj.EventQueueOverFlowCount = unpack_uatype('UInt32', data)
        return obj
    
    def __str__(self):
        return 'SubscriptionDiagnosticsDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'SessionId:' + str(self.SessionId) + ', '  + \
             'SubscriptionId:' + str(self.SubscriptionId) + ', '  + \
             'Priority:' + str(self.Priority) + ', '  + \
             'PublishingInterval:' + str(self.PublishingInterval) + ', '  + \
             'MaxKeepAliveCount:' + str(self.MaxKeepAliveCount) + ', '  + \
             'MaxLifetimeCount:' + str(self.MaxLifetimeCount) + ', '  + \
             'MaxNotificationsPerPublish:' + str(self.MaxNotificationsPerPublish) + ', '  + \
             'PublishingEnabled:' + str(self.PublishingEnabled) + ', '  + \
             'ModifyCount:' + str(self.ModifyCount) + ', '  + \
             'EnableCount:' + str(self.EnableCount) + ', '  + \
             'DisableCount:' + str(self.DisableCount) + ', '  + \
             'RepublishRequestCount:' + str(self.RepublishRequestCount) + ', '  + \
             'RepublishMessageRequestCount:' + str(self.RepublishMessageRequestCount) + ', '  + \
             'RepublishMessageCount:' + str(self.RepublishMessageCount) + ', '  + \
             'TransferRequestCount:' + str(self.TransferRequestCount) + ', '  + \
             'TransferredToAltClientCount:' + str(self.TransferredToAltClientCount) + ', '  + \
             'TransferredToSameClientCount:' + str(self.TransferredToSameClientCount) + ', '  + \
             'PublishRequestCount:' + str(self.PublishRequestCount) + ', '  + \
             'DataChangeNotificationsCount:' + str(self.DataChangeNotificationsCount) + ', '  + \
             'EventNotificationsCount:' + str(self.EventNotificationsCount) + ', '  + \
             'NotificationsCount:' + str(self.NotificationsCount) + ', '  + \
             'LatePublishRequestCount:' + str(self.LatePublishRequestCount) + ', '  + \
             'CurrentKeepAliveCount:' + str(self.CurrentKeepAliveCount) + ', '  + \
             'CurrentLifetimeCount:' + str(self.CurrentLifetimeCount) + ', '  + \
             'UnacknowledgedMessageCount:' + str(self.UnacknowledgedMessageCount) + ', '  + \
             'DiscardedMessageCount:' + str(self.DiscardedMessageCount) + ', '  + \
             'MonitoredItemCount:' + str(self.MonitoredItemCount) + ', '  + \
             'DisabledMonitoredItemCount:' + str(self.DisabledMonitoredItemCount) + ', '  + \
             'MonitoringQueueOverflowCount:' + str(self.MonitoringQueueOverflowCount) + ', '  + \
             'NextSequenceNumber:' + str(self.NextSequenceNumber) + ', '  + \
             'EventQueueOverFlowCount:' + str(self.EventQueueOverFlowCount) + ')'
    
    __repr__ = __str__
    
class ModelChangeStructureDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ModelChangeStructureDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Affected = NodeId()
        self.AffectedType = NodeId()
        self.Verb = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.Affected.to_binary())
        body.append(self.AffectedType.to_binary())
        body.append(pack_uatype('Byte', self.Verb))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ModelChangeStructureDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Affected = NodeId.from_binary(data)
        obj.AffectedType = NodeId.from_binary(data)
        obj.Verb = unpack_uatype('Byte', data)
        return obj
    
    def __str__(self):
        return 'ModelChangeStructureDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Affected:' + str(self.Affected) + ', '  + \
             'AffectedType:' + str(self.AffectedType) + ', '  + \
             'Verb:' + str(self.Verb) + ')'
    
    __repr__ = __str__
    
class SemanticChangeStructureDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.SemanticChangeStructureDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Affected = NodeId()
        self.AffectedType = NodeId()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.Affected.to_binary())
        body.append(self.AffectedType.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = SemanticChangeStructureDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Affected = NodeId.from_binary(data)
        obj.AffectedType = NodeId.from_binary(data)
        return obj
    
    def __str__(self):
        return 'SemanticChangeStructureDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Affected:' + str(self.Affected) + ', '  + \
             'AffectedType:' + str(self.AffectedType) + ')'
    
    __repr__ = __str__
    
class Range(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.Range_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Low = 0
        self.High = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Double', self.Low))
        body.append(pack_uatype('Double', self.High))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Range()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Low = unpack_uatype('Double', data)
        obj.High = unpack_uatype('Double', data)
        return obj
    
    def __str__(self):
        return 'Range(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Low:' + str(self.Low) + ', '  + \
             'High:' + str(self.High) + ')'
    
    __repr__ = __str__
    
class EUInformation(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.EUInformation_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.NamespaceUri = ''
        self.UnitId = 0
        self.DisplayName = LocalizedText()
        self.Description = LocalizedText()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.NamespaceUri))
        body.append(pack_uatype('Int32', self.UnitId))
        body.append(self.DisplayName.to_binary())
        body.append(self.Description.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = EUInformation()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.NamespaceUri = unpack_uatype('String', data)
        obj.UnitId = unpack_uatype('Int32', data)
        obj.DisplayName = LocalizedText.from_binary(data)
        obj.Description = LocalizedText.from_binary(data)
        return obj
    
    def __str__(self):
        return 'EUInformation(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'NamespaceUri:' + str(self.NamespaceUri) + ', '  + \
             'UnitId:' + str(self.UnitId) + ', '  + \
             'DisplayName:' + str(self.DisplayName) + ', '  + \
             'Description:' + str(self.Description) + ')'
    
    __repr__ = __str__
    
class ComplexNumberType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ComplexNumberType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Real = 0
        self.Imaginary = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Float', self.Real))
        body.append(pack_uatype('Float', self.Imaginary))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ComplexNumberType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Real = unpack_uatype('Float', data)
        obj.Imaginary = unpack_uatype('Float', data)
        return obj
    
    def __str__(self):
        return 'ComplexNumberType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Real:' + str(self.Real) + ', '  + \
             'Imaginary:' + str(self.Imaginary) + ')'
    
    __repr__ = __str__
    
class DoubleComplexNumberType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.DoubleComplexNumberType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Real = 0
        self.Imaginary = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Double', self.Real))
        body.append(pack_uatype('Double', self.Imaginary))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = DoubleComplexNumberType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Real = unpack_uatype('Double', data)
        obj.Imaginary = unpack_uatype('Double', data)
        return obj
    
    def __str__(self):
        return 'DoubleComplexNumberType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Real:' + str(self.Real) + ', '  + \
             'Imaginary:' + str(self.Imaginary) + ')'
    
    __repr__ = __str__
    
class AxisInformation(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.AxisInformation_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.EngineeringUnits = EUInformation()
        self.EURange = Range()
        self.Title = LocalizedText()
        self.AxisScaleType = 0
        self.AxisSteps = []
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.EngineeringUnits.to_binary())
        body.append(self.EURange.to_binary())
        body.append(self.Title.to_binary())
        body.append(pack_uatype('UInt32', self.AxisScaleType))
        body.append(struct.pack('<i', len(self.AxisSteps)))
        for fieldname in self.AxisSteps:
            body.append(pack_uatype('Double', fieldname))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = AxisInformation()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.EngineeringUnits = EUInformation.from_binary(data)
        obj.EURange = Range.from_binary(data)
        obj.Title = LocalizedText.from_binary(data)
        obj.AxisScaleType = unpack_uatype('UInt32', data)
        obj.AxisSteps = unpack_uatype_array('Double', data)
        return obj
    
    def __str__(self):
        return 'AxisInformation(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'EngineeringUnits:' + str(self.EngineeringUnits) + ', '  + \
             'EURange:' + str(self.EURange) + ', '  + \
             'Title:' + str(self.Title) + ', '  + \
             'AxisScaleType:' + str(self.AxisScaleType) + ', '  + \
             'AxisSteps:' + str(self.AxisSteps) + ')'
    
    __repr__ = __str__
    
class XVType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.XVType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.X = 0
        self.Value = 0
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('Double', self.X))
        body.append(pack_uatype('Float', self.Value))
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = XVType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.X = unpack_uatype('Double', data)
        obj.Value = unpack_uatype('Float', data)
        return obj
    
    def __str__(self):
        return 'XVType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'X:' + str(self.X) + ', '  + \
             'Value:' + str(self.Value) + ')'
    
    __repr__ = __str__
    
class ProgramDiagnosticDataType(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.ProgramDiagnosticDataType_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.CreateSessionId = NodeId()
        self.CreateClientName = ''
        self.InvocationCreationTime = DateTime()
        self.LastTransitionTime = DateTime()
        self.LastMethodCall = ''
        self.LastMethodSessionId = NodeId()
        self.LastMethodInputArguments = []
        self.LastMethodOutputArguments = []
        self.LastMethodCallTime = DateTime()
        self.LastMethodReturnStatus = StatusResult()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(self.CreateSessionId.to_binary())
        body.append(pack_uatype('String', self.CreateClientName))
        body.append(self.InvocationCreationTime.to_binary())
        body.append(self.LastTransitionTime.to_binary())
        body.append(pack_uatype('String', self.LastMethodCall))
        body.append(self.LastMethodSessionId.to_binary())
        body.append(struct.pack('<i', len(self.LastMethodInputArguments)))
        for fieldname in self.LastMethodInputArguments:
            body.append(fieldname.to_binary())
        body.append(struct.pack('<i', len(self.LastMethodOutputArguments)))
        for fieldname in self.LastMethodOutputArguments:
            body.append(fieldname.to_binary())
        body.append(self.LastMethodCallTime.to_binary())
        body.append(self.LastMethodReturnStatus.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = ProgramDiagnosticDataType()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.CreateSessionId = NodeId.from_binary(data)
        obj.CreateClientName = unpack_uatype('String', data)
        obj.InvocationCreationTime = DateTime.from_binary(data)
        obj.LastTransitionTime = DateTime.from_binary(data)
        obj.LastMethodCall = unpack_uatype('String', data)
        obj.LastMethodSessionId = NodeId.from_binary(data)
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.LastMethodInputArguments.append(Argument.from_binary(data))
        length = struct.unpack('<i', data.read(4))[0]
        if length != -1:
            for i in range(0, length):
                obj.LastMethodOutputArguments.append(Argument.from_binary(data))
        obj.LastMethodCallTime = DateTime.from_binary(data)
        obj.LastMethodReturnStatus = StatusResult.from_binary(data)
        return obj
    
    def __str__(self):
        return 'ProgramDiagnosticDataType(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'CreateSessionId:' + str(self.CreateSessionId) + ', '  + \
             'CreateClientName:' + str(self.CreateClientName) + ', '  + \
             'InvocationCreationTime:' + str(self.InvocationCreationTime) + ', '  + \
             'LastTransitionTime:' + str(self.LastTransitionTime) + ', '  + \
             'LastMethodCall:' + str(self.LastMethodCall) + ', '  + \
             'LastMethodSessionId:' + str(self.LastMethodSessionId) + ', '  + \
             'LastMethodInputArguments:' + str(self.LastMethodInputArguments) + ', '  + \
             'LastMethodOutputArguments:' + str(self.LastMethodOutputArguments) + ', '  + \
             'LastMethodCallTime:' + str(self.LastMethodCallTime) + ', '  + \
             'LastMethodReturnStatus:' + str(self.LastMethodReturnStatus) + ')'
    
    __repr__ = __str__
    
class Annotation(object):
    '''
    
    '''
    def __init__(self):
        self.TypeId = FourByteNodeId(ObjectIds.Annotation_Encoding_DefaultBinary)
        self.Encoding = 1
        self.BodyLength = 0
        self.Message = ''
        self.UserName = ''
        self.AnnotationTime = DateTime()
    
    def to_binary(self):
        packet = []
        body = []
        packet.append(self.TypeId.to_binary())
        packet.append(pack_uatype('UInt8', self.Encoding))
        body.append(pack_uatype('String', self.Message))
        body.append(pack_uatype('String', self.UserName))
        body.append(self.AnnotationTime.to_binary())
        body = b''.join(body)
        packet.append(struct.pack('<i', len(body)))
        packet.append(body)
        return b''.join(packet)
        
    @staticmethod
    def from_binary(data):
        obj = Annotation()
        obj.TypeId = NodeId.from_binary(data)
        obj.Encoding = unpack_uatype('UInt8', data)
        obj.BodyLength = unpack_uatype('Int32', data)
        obj.Message = unpack_uatype('String', data)
        obj.UserName = unpack_uatype('String', data)
        obj.AnnotationTime = DateTime.from_binary(data)
        return obj
    
    def __str__(self):
        return 'Annotation(' + 'TypeId:' + str(self.TypeId) + ', '  + \
             'Encoding:' + str(self.Encoding) + ', '  + \
             'BodyLength:' + str(self.BodyLength) + ', '  + \
             'Message:' + str(self.Message) + ', '  + \
             'UserName:' + str(self.UserName) + ', '  + \
             'AnnotationTime:' + str(self.AnnotationTime) + ')'
    
    __repr__ = __str__
