from ctypes.wintypes import *
from winusb import UsbSetupPacket, LpOverlapped, UsbInterfaceDescriptor, LpSecurityAttributes, GUID, PspDevinfoData, PspDeviceInterfaceData, Psp_Device_Interface_Detail_Data

WinUsb_Initialize = "WinUsb_Initialize"
WinUsb_ControlTransfer = "WinUsb_ControlTransfer"
WinUsb_GetDescriptor = "WinUsb_GetDescriptor"
WinUsb_ReadPipe = "WinUsb_ReadPipe"
WinUsb_WritePipe = "WinUsb_WritePipe"
WinUsb_Free = "WinUsb_Free"
WinUsb_QueryDeviceInformation = "WinUsb_QueryDeviceInformation"
WinUsb_QueryInterfaceSettings = "WinUsb_QueryInterfaceSettings"
WinUsb_QueryPipe = "WinUsb_QueryPipe"
WinUsb_ControlTransfer = "WinUsb_ControlTransfer"
Close_Handle = "CloseHandle"
CreateFileW = "CreateFileW"
ReadFile = "ReadFile"
CancelIo  = "CancelIo"
WriteFile = "WriteFile"
SetEvent  = "SetEvent"
WaitForSingleObject = "WaitForSingleObject"
SetupDiGetClassDevs  = "SetupDiGetClassDevs"
SetupDiEnumDeviceInterfaces = "SetupDiEnumDeviceInterfaces"
SetupDiGetDeviceInterfaceDetail = "SetupDiGetDeviceInterfaceDetail"

def get_winusb_functions(windll):
	""" Functions availabe from WinUsb dll and their types"""
	winusb_dict = {}
	winusb_functions = {}
	winusb_restypes = {}
	winusb_argtypes = {}

	# BOOL __stdcall WinUsb_Initialize( _In_ HANDLE DeviceHandle,_Out_  PWINUSB_INTERFACE_HANDLE InterfaceHandle);
	winusb_functions[WinUsb_Initialize] = windll.WinUsb_Initialize
	winusb_restypes[WinUsb_Initialize] = BOOL
	winusb_argtypes[WinUsb_Initialize] = [HANDLE, c_void_p]

	#BOOL __stdcall WinUsb_ControlTransfer(_In_ WINUSB_INTERFACE_HANDLE InterfaceHandle,_In_ WINUSB_SETUP_PACKET SetupPacket, _Out_ PUCHAR Buffer,_In_ ULONG BufferLength,_Out_opt_  PULONG LengthTransferred,_In_opt_  LPOVERLAPPED Overlapped);
	winusb_functions[WinUsb_ControlTransfer] = windll.WinUsb_ControlTransfer
	winusb_restypes[WinUsb_ControlTransfer] = BOOL
	winusb_argtypes[WinUsb_ControlTransfer] = [c_void_p, UsbSetupPacket, pointer(c_ubyte), c_ulong, pointer(c_ulong), LpOverlapped] 

	#BOOL __stdcall WinUsb_GetDescriptor(_In_ WINUSB_INTERFACE_HANDLE InterfaceHandle,_In_ UCHAR DescriptorType,_In_ UCHAR Index,_In_ USHORT LanguageID,_Out_ PUCHAR Buffer,_In_ ULONG BufferLength,_Out_ PULONG LengthTransferred);
	winusb_functions[WinUsb_GetDescriptor] = windll.WinUsb_GetDescriptor
	winusb_restypes[WinUsb_GetDescriptor] = BOOL
	winusb_argtypes[WinUsb_GetDescriptor] = [c_void_p, c_ubyte, c_ubyte, c_ushort, pointer(c_ubyte), c_ulong, pointer(c_ulong)]

	#BOOL __stdcall WinUsb_ReadPipe( _In_ WINUSB_INTERFACE_HANDLE InterfaceHandle,_In_ UCHAR PipeID,_Out_ PUCHAR Buffer,_In_ ULONG BufferLength,_Out_opt_ PULONG LengthTransferred,_In_opt_ LPOVERLAPPED Overlapped);
	winusb_functions[WinUsb_ReadPipe] = windll.WinUsb_ReadPipe
	winusb_restypes[WinUsb_ReadPipe] = BOOL
	winusb_argtypes[WinUsb_ReadPipe] = [c_void_p, c_ubyte, pointer(c_ubyte), c_ulong, pointer(c_ulong), LpOverlapped]

	#BOOL __stdcall WinUsb_WritePipe(_In_ WINUSB_INTERFACE_HANDLE InterfaceHandle,_In_ UCHAR PipeID,_In_ PUCHAR Buffer,_In_ ULONG BufferLength,_Out_opt_  PULONG LengthTransferred,_In_opt_ LPOVERLAPPED Overlapped);
	winusb_functions[WinUsb_WritePipe] = windll.WinUsb_WritePipe
	winusb_restypes[WinUsb_WritePipe] = BOOL
	winusb_argtypes[WinUsb_WritePipe] = [c_void_p, c_ubyte, pointer(c_ubyte), c_ulong, pointer(c_ulong), LpOverlapped]

	#BOOL __stdcall WinUsb_Free(_In_ WINUSB_INTERFACE_HANDLE InterfaceHandle);
	winusb_functions[WinUsb_Free] = windll.WinUsb_Free
	winusb_restypes[WinUsb_Free] = BOOL
	winusb_argtypes[WinUsb_Free] = [c_void_p]

	#BOOL __stdcall WinUsb_QueryDeviceInformation(_In_ WINUSB_INTERFACE_HANDLE InterfaceHandle,_In_ ULONG InformationType,_Inout_ PULONG BufferLength,_Out_ PVOID Buffer);
	winusb_functions[WinUsb_QueryDeviceInformation] = windll.WinUsb_QueryDeviceInformation
	winusb_restypes = BOOL
	winusb_argtypes = [c_void_p, c_ulong, pointer(c_ulong), c_void_p]

	#BOOL __stdcall WinUsb_QueryInterfaceSettings(_In_ WINUSB_INTERFACE_HANDLE InterfaceHandle,_In_ UCHAR AlternateSettingNumber,_Out_ PUSB_INTERFACE_DESCRIPTOR UsbAltInterfaceDescriptor);
	winusb_functions[WinUsb_QueryInterfaceSettings] = windll.WinUsb_QueryInterfaceSettings
	winusb_restypes[WinUsb_QueryInterfaceSettings] = BOOL
	winusb_argtypes[WinUsb_QueryInterfaceSettings] = [c_void_p, c_ubyte, UsbInterfaceDescriptor]

	winusb_dict["functions"] = winusb_functions 
	winusb_dict["restypes"] = winusb_restypes
	winusb_dict["argtypes"] = winusb_argtypes
	return winusb_dict

def get_kernel32_functions(kernel32):
	kernel32_dict = {}
	kernel32_functions = {}
	kernel32_restypes = {}
	kernel32_argtypes = {}

	#BOOL WINAPI CloseHandle(_In_  HANDLE hObject);
	kernel32_functions[Close_Handle] = kernel32.CloseHandle
	kernel32_restypes[Close_Handle] = BOOL
	kernel32_argtypes[Close_Handle] = [HANDLE]

	#BOOL WINAPI ReadFile(_In_ HANDLE hFile,_Out_ LPVOID lpBuffer,_In_ DWORD nNumberOfBytesToRead,_Out_opt_ LPDWORD lpNumberOfBytesRead,_Inout_opt_ LPOVERLAPPED lpOverlapped);
	kernel32_functions[ReadFile] = kernel32.ReadFile
	kernel32_restypes[ReadFile] = BOOL
	kernel32_argtypes[ReadFile] = [HANDLE, c_void_p, DWORD, pointer(DWORD), LpOverlapped]

	#BOOL WINAPI CancelIo(_In_  HANDLE hFile);
	kernel32_functions[CancelIo] = kernel32.CancelIo
	kernel32_restypes[CancelIo] = BOOL
	kernel32_argtypes[CancelIo] = [HANDLE]

	#BOOL WINAPI WriteFile(_In_ HANDLE hFile,_In_ LPCVOID lpBuffer,_In_ DWORD nNumberOfBytesToWrite,_Out_opt_ LPDWORD lpNumberOfBytesWritten,_Inout_opt_  LPOVERLAPPED lpOverlapped);
	kernel32_functions[WriteFile] = kernel32.WriteFile
	kernel32_restypes[WriteFile] = BOOL
	kernel32_argtypes[WriteFile] = [HANDLE, c_void_p, DWORD, pointer(DWORD), LpOverlapped]

	#BOOL WINAPI SetEvent(_In_ HANDLE hEvent);
	kernel32_functions[SetEvent] = kernel32.SetEvent
	kernel32_restypes[SetEvent] = BOOL
	kernel32_argtypes[SetEvent] = [HANDLE]

	#DWORD WINAPI WaitForSingleObject(_In_ HANDLE hHandle, _In_  DWORD dwMilliseconds);
	kernel32_functions[WaitForSingleObject] = kernel32.WaitForSingleObject
	kernel32_restypes[WaitForSingleObject] = DWORD
	kernel32_argtypes[WaitForSingleObject] = [HANDLE, DWORD]

	#HANDLE WINAPI CreateFile(_In_ LPCTSTR lpFileName,_In_ DWORD dwDesiredAccess,_In_ DWORD dwShareMode,_In_opt_ LPSECURITY_ATTRIBUTES lpSecurityAttributes,_In_ DWORD dwCreationDisposition,_In_ DWORD dwFlagsAndAttributes,_In_opt_ HANDLE hTemplateFile);
	kernel32_functions[CreateFileW] = kernel32.CreateFileW 
	kernel32_restypes[CreateFileW] = HANDLE
	kernel32_argtypes[CreateFileW] = [c_wchar_p, DWORD, DWORD, LpSecurityAttributes, DWORD, DWORD, HANDLE]

	kernel32_dict["functions"] = kernel32_functions
	kernel32_dict["restypes"] = kernel32_restypes
	kernel32_dict["argtypes"] = kernel32_argtypes
	return kernel32_dict

def get_setupapi_functions(setupapi):
	setupapi_dict = {}
	setupapi_functions = {}
	setupapi_restypes = {}
	setupapi_argtypes = {}

	#HDEVINFO SetupDiGetClassDevs(_In_opt_ const GUID *ClassGuid,_In_opt_ PCTSTR Enumerator,_In_opt_ HWND hwndParent,_In_ DWORD Flags);
	setupapi_functions[SetupDiGetClassDevs] = setupapi.SetupDiGetClassDevs
	setupapi_restypes[SetupDiGetClassDevs] = c_void_p
	setupapi_argtypes[SetupDiGetClassDevs] = [GUID, c_wchar_p, HANDLE, DWORD]

	#BOOL SetupDiEnumDeviceInterfaces(_In_ HDEVINFO DeviceInfoSet,_In_opt_ PSP_DEVINFO_DATA DeviceInfoData,_In_ const GUID *InterfaceClassGuid,_In_ DWORD MemberIndex,_Out_ PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData);
	setupapi_functions[SetupDiEnumDeviceInterfaces] = setupapi.SetupDiEnumDeviceInterfaces
	setupapi_restypes[SetupDiEnumDeviceInterfaces] = BOOL
	setupapi_argtypes[SetupDiEnumDeviceInterfaces] = [c_void_p, PspDevinfoData, pointer(GUID), DWORD, PspDeviceInterfaceData]

	#BOOL SetupDiGetDeviceInterfaceDetail(_In_ HDEVINFO DeviceInfoSet,_In_ PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,_Out_opt_ PSP_DEVICE_INTERFACE_DETAIL_DATA DeviceInterfaceDetailData,_In_ DWORD DeviceInterfaceDetailDataSize,_Out_opt_  PDWORD RequiredSize,_Out_opt_  PSP_DEVINFO_DATA DeviceInfoData);
	setupapi_functions[SetupDiGetDeviceInterfaceDetail] = setupapi.SetupDiGetDeviceInterfaceDetail
	setupapi_restypes[SetupDiGetDeviceInterfaceDetail] = BOOL
	setupapi_argtypes[SetupDiGetDeviceInterfaceDetail] = [c_void_p, PspDeviceInterfaceData, Psp_Device_Interface_Detail_Data, DWORD, DWORD, PspDevinfoData]

	setupapi_dict["functions"] = setupapi_functions
	setupapi_dict["restypes"] = setupapi_restypes
	setupapi_dict["argtypes"] = setupapi_argtypes 
	return setupapi_dict