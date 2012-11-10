# coding: utf-8
"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.

In case you're wondering, I generated this by parsing the Python headers, and then scraping the Python API documentation
site for descriptions of each function.
"""
from _kernel32 import *
from pyctypes import *

def populate_exports(dll):
	try:
		dll._PyObject_GC_Malloc.restype = POINTER(PyObject)
		dll._PyObject_GC_Malloc.argtypes = [ c_size_t ]
		dll._PyObject_GC_New.restype = POINTER(PyObject)
		dll._PyObject_GC_New.argtypes = [ POINTER(py_object) ]
		dll._PyObject_GC_NewVar.restype = POINTER(PyVarObject)
		dll._PyObject_GC_NewVar.argtypes = [ POINTER(py_object), c_ssize_t ]
		dll.PyObject_GC_Track.restype = None
		dll.PyObject_GC_Track.argtypes = [ c_void_p ]
		dll.PyObject_GC_Track.__doc__ = """Adds the object op to the set of container objects tracked by the
	collector.  The collector can run at unexpected times so objects must be
	valid while being tracked.  This should be called once all the fields
	followed by the tp_traverse handler become valid, usually near the
	end of the constructor."""
		dll.PyObject_GC_UnTrack.restype = None
		dll.PyObject_GC_UnTrack.argtypes = [ c_void_p ]
		dll.PyObject_GC_UnTrack.__doc__ = """Remove the object op from the set of container objects tracked by the
	collector.  Note that PyObject_GC_Track() can be called again on
	this object to add it back to the set of tracked objects.  The deallocator
	( tp_dealloc handler) should call this for the object before any of
	the fields used by the tp_traverse handler become invalid."""
		dll.PyObject_GC_Del.restype = None
		dll.PyObject_GC_Del.argtypes = [ c_void_p ]
		dll.PyObject_GC_Del.__doc__ = """Releases memory allocated to an object using PyObject_GC_New() or PyObject_GC_NewVar() ."""
		dll.Py_FatalError.restype = None
		dll.Py_FatalError.argtypes = [ c_char_p ]
		dll.Py_FatalError.__doc__ = """Print a fatal error message and kill the process.  No cleanup is performed.
	This function should only be invoked when a condition is detected that would
	make it dangerous to continue using the Python interpreter; e.g., when the
	object administration appears to be corrupted.  On Unix, the standard C library
	function abort() is called which will attempt to produce a core file."""
		dll.PyUnicodeUCS2_FromUnicode.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromUnicode.argtypes = [ c_wchar_p, c_ssize_t ]
		dll.PyUnicodeUCS2_FromStringAndSize.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromStringAndSize.argtypes = [ c_char_p, c_ssize_t ]
		dll.PyUnicodeUCS2_FromString.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromString.argtypes = [ c_char_p ]
		dll.PyUnicodeUCS2_AsUnicode.restype = c_wchar_p
		dll.PyUnicodeUCS2_AsUnicode.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_GetSize.restype = c_ssize_t
		dll.PyUnicodeUCS2_GetSize.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_GetMax.restype = c_wchar
		dll.PyUnicodeUCS2_GetMax.argtypes = [  ]
		dll.PyUnicodeUCS2_Resize.restype = c_int
		dll.PyUnicodeUCS2_Resize.argtypes = [ POINTER(POINTER(PyObject)), c_ssize_t ]
		dll.PyUnicodeUCS2_FromEncodedObject.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromEncodedObject.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyUnicodeUCS2_FromObject.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromObject.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_FromFormatV.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromFormatV.argtypes = [ c_char_p, va_list ]
		dll.PyUnicodeUCS2_FromFormat.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromFormat.argtypes = [ c_char_p, va_list ]
		dll._PyUnicode_FormatAdvanced.restype = POINTER(PyObject)
		dll._PyUnicode_FormatAdvanced.argtypes = [ POINTER(PyObject), c_wchar_p, c_ssize_t ]
		dll.PyUnicodeUCS2_FromWideChar.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromWideChar.argtypes = [ c_wchar_p, c_ssize_t ]
		dll.PyUnicodeUCS2_AsWideChar.restype = c_ssize_t
		dll.PyUnicodeUCS2_AsWideChar.argtypes = [ POINTER(py_object), c_wchar_p, c_ssize_t ]
		dll.PyUnicodeUCS2_FromOrdinal.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_FromOrdinal.argtypes = [ c_int ]
		dll.PyUnicodeUCS2_ClearFreelist.restype = c_int
		dll.PyUnicodeUCS2_ClearFreelist.argtypes = [  ]
		dll._PyUnicodeUCS2_AsDefaultEncodedString.restype = POINTER(PyObject)
		dll._PyUnicodeUCS2_AsDefaultEncodedString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyUnicodeUCS2_GetDefaultEncoding.restype = c_char_p
		dll.PyUnicodeUCS2_GetDefaultEncoding.argtypes = [  ]
		dll.PyUnicodeUCS2_SetDefaultEncoding.restype = c_int
		dll.PyUnicodeUCS2_SetDefaultEncoding.argtypes = [ c_char_p ]
		dll.PyUnicodeUCS2_Decode.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Decode.argtypes = [ c_char_p, c_ssize_t, c_char_p, c_char_p ]
		dll.PyUnicodeUCS2_Encode.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Encode.argtypes = [ c_wchar_p, c_ssize_t, c_char_p, c_char_p ]
		dll.PyUnicodeUCS2_AsEncodedObject.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsEncodedObject.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyUnicodeUCS2_AsEncodedString.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsEncodedString.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyUnicode_BuildEncodingMap.restype = POINTER(PyObject)
		dll.PyUnicode_BuildEncodingMap.argtypes = [ POINTER(py_object) ]
		dll.PyUnicode_DecodeUTF7.restype = POINTER(PyObject)
		dll.PyUnicode_DecodeUTF7.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicode_DecodeUTF7.__doc__ = """Create a Unicode object by decoding size bytes of the UTF-7 encoded string s .  Return NULL if an exception was raised by the codec."""
		dll.PyUnicode_DecodeUTF7Stateful.restype = POINTER(PyObject)
		dll.PyUnicode_DecodeUTF7Stateful.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_ssize_t) ]
		dll.PyUnicode_DecodeUTF7Stateful.__doc__ = """If consumed is NULL , behave like PyUnicode_DecodeUTF7() .  If consumed is not NULL , trailing incomplete UTF-7 base-64 sections will not
	be treated as an error.  Those bytes will not be decoded and the number of
	bytes that have been decoded will be stored in consumed ."""
		dll.PyUnicode_EncodeUTF7.restype = POINTER(PyObject)
		dll.PyUnicode_EncodeUTF7.argtypes = [ c_wchar_p, c_ssize_t, c_int, c_int, c_char_p ]
		dll.PyUnicode_EncodeUTF7.__doc__ = """Encode the Py_UNICODE buffer of the given size using UTF-7 and
	return a Python bytes object.  Return NULL if an exception was raised by
	the codec. If base64SetO is nonzero, "Set O" (punctuation that has no otherwise
	special meaning) will be encoded in base-64.  If base64WhiteSpace is
	nonzero, whitespace will be encoded in base-64.  Both are set to zero for the
	Python "utf-7" codec."""
		dll.PyUnicodeUCS2_DecodeUTF8.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUTF8.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_DecodeUTF8Stateful.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUTF8Stateful.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_ssize_t) ]
		dll.PyUnicodeUCS2_AsUTF8String.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsUTF8String.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeUTF8.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeUTF8.argtypes = [ c_wchar_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_DecodeUTF32.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUTF32.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_int) ]
		dll.PyUnicodeUCS2_DecodeUTF32Stateful.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUTF32Stateful.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_int), POINTER(c_ssize_t) ]
		dll.PyUnicodeUCS2_AsUTF32String.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsUTF32String.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeUTF32.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeUTF32.argtypes = [ c_wchar_p, c_ssize_t, c_char_p, c_int ]
		dll.PyUnicodeUCS2_DecodeUTF16.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUTF16.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_int) ]
		dll.PyUnicodeUCS2_DecodeUTF16Stateful.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUTF16Stateful.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_int), POINTER(c_ssize_t) ]
		dll.PyUnicodeUCS2_AsUTF16String.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsUTF16String.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeUTF16.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeUTF16.argtypes = [ c_wchar_p, c_ssize_t, c_char_p, c_int ]
		dll.PyUnicodeUCS2_DecodeUnicodeEscape.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeUnicodeEscape.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_AsUnicodeEscapeString.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsUnicodeEscapeString.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeUnicodeEscape.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeUnicodeEscape.argtypes = [ c_wchar_p, c_ssize_t ]
		dll.PyUnicodeUCS2_DecodeRawUnicodeEscape.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeRawUnicodeEscape.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_AsRawUnicodeEscapeString.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsRawUnicodeEscapeString.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeRawUnicodeEscape.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeRawUnicodeEscape.argtypes = [ c_wchar_p, c_ssize_t ]
		dll._PyUnicode_DecodeUnicodeInternal.restype = POINTER(PyObject)
		dll._PyUnicode_DecodeUnicodeInternal.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_DecodeLatin1.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeLatin1.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_AsLatin1String.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsLatin1String.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeLatin1.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeLatin1.argtypes = [ c_wchar_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_DecodeASCII.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeASCII.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_AsASCIIString.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsASCIIString.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeASCII.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeASCII.argtypes = [ c_wchar_p, c_ssize_t, c_char_p ]
		dll.PyUnicodeUCS2_DecodeCharmap.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_DecodeCharmap.argtypes = [ c_char_p, c_ssize_t, POINTER(PyObject), c_char_p ]
		dll.PyUnicodeUCS2_AsCharmapString.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_AsCharmapString.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_EncodeCharmap.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_EncodeCharmap.argtypes = [ c_wchar_p, c_ssize_t, POINTER(PyObject), c_char_p ]
		dll.PyUnicodeUCS2_TranslateCharmap.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_TranslateCharmap.argtypes = [ c_wchar_p, c_ssize_t, POINTER(PyObject), c_char_p ]
		dll.PyUnicode_DecodeMBCS.restype = POINTER(PyObject)
		dll.PyUnicode_DecodeMBCS.argtypes = [ c_char_p, c_ssize_t, c_char_p ]
		dll.PyUnicode_DecodeMBCS.__doc__ = """Return value: New reference. Create a Unicode object by decoding size bytes of the MBCS encoded string s .
	Return NULL if an exception was raised by the codec. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyUnicode_DecodeMBCSStateful.restype = POINTER(PyObject)
		dll.PyUnicode_DecodeMBCSStateful.argtypes = [ c_char_p, c_ssize_t, c_char_p, POINTER(c_ssize_t) ]
		dll.PyUnicode_DecodeMBCSStateful.__doc__ = """If consumed is NULL , behave like PyUnicode_DecodeMBCS() . If consumed is not NULL , PyUnicode_DecodeMBCSStateful() will not decode
	trailing lead byte and the number of bytes that have been decoded will be stored
	in consumed . New in version 2.5."""
		dll.PyUnicode_AsMBCSString.restype = POINTER(PyObject)
		dll.PyUnicode_AsMBCSString.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicode_AsMBCSString.__doc__ = """Return value: New reference. Encode a Unicode object using MBCS and return the result as Python string
	object.  Error handling is "strict".  Return NULL if an exception was raised
	by the codec."""
		dll.PyUnicode_EncodeMBCS.restype = POINTER(PyObject)
		dll.PyUnicode_EncodeMBCS.argtypes = [ c_wchar_p, c_ssize_t, c_char_p ]
		dll.PyUnicode_EncodeMBCS.__doc__ = """Return value: New reference. Encode the Py_UNICODE buffer of the given size using MBCS and return a
	Python string object.  Return NULL if an exception was raised by the codec. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyUnicodeUCS2_EncodeDecimal.restype = c_int
		dll.PyUnicodeUCS2_EncodeDecimal.argtypes = [ c_wchar_p, c_ssize_t, c_char_p, c_char_p ]
		dll.PyUnicodeUCS2_Concat.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Concat.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_Split.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Split.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeUCS2_Splitlines.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Splitlines.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyUnicodeUCS2_Partition.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Partition.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_RPartition.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_RPartition.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_RSplit.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_RSplit.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeUCS2_Translate.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Translate.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_char_p ]
		dll.PyUnicodeUCS2_Join.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Join.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_Tailmatch.restype = c_ssize_t
		dll.PyUnicodeUCS2_Tailmatch.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_ssize_t, c_ssize_t, c_int ]
		dll.PyUnicodeUCS2_Find.restype = c_ssize_t
		dll.PyUnicodeUCS2_Find.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_ssize_t, c_ssize_t, c_int ]
		dll.PyUnicodeUCS2_Count.restype = c_ssize_t
		dll.PyUnicodeUCS2_Count.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PyUnicodeUCS2_Replace.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Replace.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeUCS2_Compare.restype = c_int
		dll.PyUnicodeUCS2_Compare.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_RichCompare.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_RichCompare.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_int ]
		dll.PyUnicodeUCS2_Format.restype = POINTER(PyObject)
		dll.PyUnicodeUCS2_Format.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyUnicodeUCS2_Contains.restype = c_int
		dll.PyUnicodeUCS2_Contains.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll._PyUnicode_XStrip.restype = POINTER(PyObject)
		dll._PyUnicode_XStrip.argtypes = [ POINTER(py_object), c_int, POINTER(PyObject) ]
		dll._PyUnicodeUCS2_IsLowercase.restype = c_int
		dll._PyUnicodeUCS2_IsLowercase.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsUppercase.restype = c_int
		dll._PyUnicodeUCS2_IsUppercase.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsTitlecase.restype = c_int
		dll._PyUnicodeUCS2_IsTitlecase.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsWhitespace.restype = c_int
		dll._PyUnicodeUCS2_IsWhitespace.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsLinebreak.restype = c_int
		dll._PyUnicodeUCS2_IsLinebreak.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_ToLowercase.restype = c_wchar
		dll._PyUnicodeUCS2_ToLowercase.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_ToUppercase.restype = c_wchar
		dll._PyUnicodeUCS2_ToUppercase.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_ToTitlecase.restype = c_wchar
		dll._PyUnicodeUCS2_ToTitlecase.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_ToDecimalDigit.restype = c_int
		dll._PyUnicodeUCS2_ToDecimalDigit.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_ToDigit.restype = c_int
		dll._PyUnicodeUCS2_ToDigit.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_ToNumeric.restype = c_double
		dll._PyUnicodeUCS2_ToNumeric.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsDecimalDigit.restype = c_int
		dll._PyUnicodeUCS2_IsDecimalDigit.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsDigit.restype = c_int
		dll._PyUnicodeUCS2_IsDigit.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsNumeric.restype = c_int
		dll._PyUnicodeUCS2_IsNumeric.argtypes = [ c_wchar ]
		dll._PyUnicodeUCS2_IsAlpha.restype = c_int
		dll._PyUnicodeUCS2_IsAlpha.argtypes = [ c_wchar ]
		dll.PyInt_FromString.restype = POINTER(PyObject)
		dll.PyInt_FromString.argtypes = [ c_char_p, POINTER(c_char_p), c_int ]
		dll.PyInt_FromString.__doc__ = """Return value: New reference. Return a new PyIntObject or PyLongObject based on the string
	value in str , which is interpreted according to the radix in base .  If pend is non- NULL , *pend will point to the first character in str which
	follows the representation of the number.  If base is 0 , the radix will be
	determined based on the leading characters of str : if str starts with '0x' or '0X' , radix 16 will be used; if str starts with '0' , radix
	8 will be used; otherwise radix 10 will be used.  If base is not 0 , it
	must be between 2 and 36 , inclusive.  Leading spaces are ignored.  If
	there are no digits, ValueError will be raised.  If the string represents
	a number too large to be contained within the machine's long c_int type
	and overflow warnings are being suppressed, a PyLongObject will be
	returned.  If overflow warnings are not being suppressed, NULL will be
	returned in this case."""
		dll.PyInt_FromUnicode.restype = POINTER(PyObject)
		dll.PyInt_FromUnicode.argtypes = [ c_wchar_p, c_ssize_t, c_int ]
		dll.PyInt_FromLong.restype = POINTER(PyObject)
		dll.PyInt_FromLong.argtypes = [ c_long ]
		dll.PyInt_FromLong.__doc__ = """Return value: New reference. Create a new integer object with a value of ival . The current implementation keeps an array of integer objects for all integers
	between -5 and 256 , when you create an c_int in that range you actually
	just get back a reference to the existing object. So it should be possible to
	change the value of 1 .  I suspect the behaviour of Python in this case is
	undefined. :-)"""
		dll.PyInt_FromSize_t.restype = POINTER(PyObject)
		dll.PyInt_FromSize_t.argtypes = [ c_size_t ]
		dll.PyInt_FromSize_t.__doc__ = """Create a new integer object with a value of ival . If the value exceeds LONG_MAX , a long integer object is returned. New in version 2.5."""
		dll.PyInt_FromSsize_t.restype = POINTER(PyObject)
		dll.PyInt_FromSsize_t.argtypes = [ c_ssize_t ]
		dll.PyInt_FromSsize_t.__doc__ = """Return value: New reference. Create a new integer object with a value of ival . If the value is larger
	than LONG_MAX or smaller than LONG_MIN , a long integer object is
	returned. New in version 2.5."""
		dll.PyInt_AsLong.restype = c_long
		dll.PyInt_AsLong.argtypes = [ POINTER(PyObject) ]
		dll.PyInt_AsLong.__doc__ = """Will first attempt to cast the object to a PyIntObject , if it is not
	already one, and then return its value. If there is an error, -1 is
	returned, and the caller should check PyErr_Occurred() to find out whether
	there was an error, or whether the value just happened to be -1."""
		dll.PyInt_AsSsize_t.restype = c_ssize_t
		dll.PyInt_AsSsize_t.argtypes = [ POINTER(PyObject) ]
		dll.PyInt_AsSsize_t.__doc__ = """Will first attempt to cast the object to a PyIntObject or PyLongObject , if it is not already one, and then return its value as Py_ssize_t . New in version 2.5."""
		dll.PyInt_AsUnsignedLongMask.restype = c_ulong
		dll.PyInt_AsUnsignedLongMask.argtypes = [ POINTER(PyObject) ]
		dll.PyInt_AsUnsignedLongMask.__doc__ = """Will first attempt to cast the object to a PyIntObject or PyLongObject , if it is not already one, and then return its value as
	unsigned long.  This function does not check for overflow. New in version 2.3."""
		dll.PyInt_AsUnsignedLongLongMask.restype = c_uint64
		dll.PyInt_AsUnsignedLongLongMask.argtypes = [ POINTER(PyObject) ]
		dll.PyInt_AsUnsignedLongLongMask.__doc__ = """Will first attempt to cast the object to a PyIntObject or PyLongObject , if it is not already one, and then return its value as
	unsigned long long, without checking for overflow. New in version 2.3."""
		dll.PyInt_GetMax.restype = c_long
		dll.PyInt_GetMax.argtypes = [  ]
		dll.PyInt_GetMax.__doc__ = """Return the system's idea of the largest integer it can handle
	( LONG_MAX , as defined in the system header files)."""
		dll.PyOS_strtoul.restype = c_ulong
		dll.PyOS_strtoul.argtypes = [ c_char_p, POINTER(c_char_p), c_int ]
		dll.PyOS_strtol.restype = c_long
		dll.PyOS_strtol.argtypes = [ c_char_p, POINTER(c_char_p), c_int ]
		dll.PyInt_ClearFreeList.restype = c_int
		dll.PyInt_ClearFreeList.argtypes = [  ]
		dll.PyInt_ClearFreeList.__doc__ = """Clear the integer free list. Return the number of items that could not
	be freed. New in version 2.6."""
		dll._PyInt_Format.restype = POINTER(PyObject)
		dll._PyInt_Format.argtypes = [ POINTER(py_object), c_int, c_int ]
		dll._PyInt_FormatAdvanced.restype = POINTER(PyObject)
		dll._PyInt_FormatAdvanced.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t ]
		dll.PyBool_FromLong.restype = POINTER(PyObject)
		dll.PyBool_FromLong.argtypes = [ c_long ]
		dll.PyBool_FromLong.__doc__ = """Return value: New reference. Return a new reference to Py_True or Py_False depending on the
	truth value of v . New in version 2.3."""
		dll.PyLong_FromLong.restype = POINTER(PyObject)
		dll.PyLong_FromLong.argtypes = [ c_long ]
		dll.PyLong_FromLong.__doc__ = """Return value: New reference. Return a new PyLongObject object from v , or NULL on failure."""
		dll.PyLong_FromUnsignedLong.restype = POINTER(PyObject)
		dll.PyLong_FromUnsignedLong.argtypes = [ c_ulong ]
		dll.PyLong_FromUnsignedLong.__doc__ = """Return value: New reference. Return a new PyLongObject object from a C unsigned long , or NULL on failure."""
		dll.PyLong_FromDouble.restype = POINTER(PyObject)
		dll.PyLong_FromDouble.argtypes = [ c_double ]
		dll.PyLong_FromDouble.__doc__ = """Return value: New reference. Return a new PyLongObject object from the integer part of v , or NULL on failure."""
		dll.PyLong_FromSize_t.restype = POINTER(PyObject)
		dll.PyLong_FromSize_t.argtypes = [ c_size_t ]
		dll.PyLong_FromSize_t.__doc__ = """Return value: New reference. Return a new PyLongObject object from a C size_t , or NULL on failure. New in version 2.6."""
		dll.PyLong_FromSsize_t.restype = POINTER(PyObject)
		dll.PyLong_FromSsize_t.argtypes = [ c_ssize_t ]
		dll.PyLong_FromSsize_t.__doc__ = """Return value: New reference. Return a new PyLongObject object from a C Py_ssize_t , or NULL on failure. New in version 2.6."""
		dll.PyLong_AsLong.restype = c_long
		dll.PyLong_AsLong.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsLong.__doc__ = """Return a C long representation of the contents of pylong .  If pylong is greater than LONG_MAX , an OverflowError is raised
	and -1 will be returned."""
		dll.PyLong_AsLongAndOverflow.restype = c_long
		dll.PyLong_AsLongAndOverflow.argtypes = [ POINTER(PyObject), POINTER(c_int) ]
		dll.PyLong_AsLongAndOverflow.__doc__ = """Return a C long representation of the contents of pylong .  If pylong is greater than LONG_MAX or less
	than LONG_MIN , set *overflow to 1 or -1 ,
	respectively, and return -1 ; otherwise, set *overflow to 0 .  If any other exception occurs (for example a TypeError or
	MemoryError), then -1 will be returned and *overflow will
	be 0 . New in version 2.7."""
		dll.PyLong_AsUnsignedLong.restype = c_ulong
		dll.PyLong_AsUnsignedLong.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsUnsignedLong.__doc__ = """Return a C unsigned long representation of the contents of pylong .
	If pylong is greater than ULONG_MAX , an OverflowError is
	raised."""
		dll.PyLong_AsUnsignedLongMask.restype = c_ulong
		dll.PyLong_AsUnsignedLongMask.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsUnsignedLongMask.__doc__ = """Return a C unsigned long from a Python long integer, without checking
	for overflow. New in version 2.3."""
		dll.PyLong_AsSsize_t.restype = c_ssize_t
		dll.PyLong_AsSsize_t.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsSsize_t.__doc__ = """Return a C Py_ssize_t representation of the contents of pylong .  If pylong is greater than PY_SSIZE_T_MAX , an OverflowError is raised
	and -1 will be returned. New in version 2.6."""
		dll.PyLong_GetInfo.restype = POINTER(PyObject)
		dll.PyLong_GetInfo.argtypes = [  ]
		dll._PyLong_Frexp.restype = c_double
		dll._PyLong_Frexp.argtypes = [ POINTER(py_object), POINTER(c_ssize_t) ]
		dll.PyLong_AsDouble.restype = c_double
		dll.PyLong_AsDouble.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsDouble.__doc__ = """Return a C double representation of the contents of pylong .  If pylong cannot be approximately represented as a double , an OverflowError exception is raised and -1.0 will be returned."""
		dll.PyLong_FromVoidPtr.restype = POINTER(PyObject)
		dll.PyLong_FromVoidPtr.argtypes = [ c_void_p ]
		dll.PyLong_FromVoidPtr.__doc__ = """Return value: New reference. Create a Python integer or long integer from the pointer p . The pointer value
	can be retrieved from the resulting value using PyLong_AsVoidPtr() . New in version 1.5.2. Changed in version 2.5: If the integer is larger than LONG_MAX, a positive long integer is returned."""
		dll.PyLong_AsVoidPtr.restype = c_void_p
		dll.PyLong_AsVoidPtr.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsVoidPtr.__doc__ = """Convert a Python integer or long integer pylong to a C void pointer.
	If pylong cannot be converted, an OverflowError will be raised.  This
	is only assured to produce a usable void pointer for values created
	with PyLong_FromVoidPtr() . New in version 1.5.2. Changed in version 2.5: For values outside 0..LONG_MAX, both signed and unsigned integers are accepted."""
		dll.PyLong_FromLongLong.restype = POINTER(PyObject)
		dll.PyLong_FromLongLong.argtypes = [ c_int64 ]
		dll.PyLong_FromLongLong.__doc__ = """Return value: New reference. Return a new PyLongObject object from a C long long , or NULL on failure."""
		dll.PyLong_FromUnsignedLongLong.restype = POINTER(PyObject)
		dll.PyLong_FromUnsignedLongLong.argtypes = [ c_ulonglong ]
		dll.PyLong_FromUnsignedLongLong.__doc__ = """Return value: New reference. Return a new PyLongObject object from a C unsigned long long ,
	or NULL on failure."""
		dll.PyLong_AsLongLong.restype = c_int64
		dll.PyLong_AsLongLong.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsLongLong.__doc__ = """Return a C long long from a Python long integer.  If pylong cannot be represented as a long long , an OverflowError is raised and -1 is returned. New in version 2.2."""
		dll.PyLong_AsUnsignedLongLong.restype = c_uint64
		dll.PyLong_AsUnsignedLongLong.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsUnsignedLongLong.__doc__ = """Return a C unsigned long long from a Python long integer. If pylong cannot be represented as an unsigned long long , an OverflowError is raised and (unsigned long long)-1 is
	returned. New in version 2.2. Changed in version 2.7: A negative pylong now raises OverflowError , not TypeError ."""
		dll.PyLong_AsUnsignedLongLongMask.restype = c_uint64
		dll.PyLong_AsUnsignedLongLongMask.argtypes = [ POINTER(PyObject) ]
		dll.PyLong_AsUnsignedLongLongMask.__doc__ = """Return a C unsigned long long from a Python long integer, without
	checking for overflow. New in version 2.3."""
		dll.PyLong_AsLongLongAndOverflow.restype = c_int64
		dll.PyLong_AsLongLongAndOverflow.argtypes = [ POINTER(PyObject), POINTER(c_int) ]
		dll.PyLong_AsLongLongAndOverflow.__doc__ = """Return a C long long representation of the contents of pylong .  If pylong is greater than PY_LLONG_MAX or less
	than PY_LLONG_MIN , set *overflow to 1 or -1 ,
	respectively, and return -1 ; otherwise, set *overflow to 0 .  If any other exception occurs (for example a TypeError or
	MemoryError), then -1 will be returned and *overflow will
	be 0 . New in version 2.7."""
		dll.PyLong_FromString.restype = POINTER(PyObject)
		dll.PyLong_FromString.argtypes = [ c_char_p, POINTER(c_char_p), c_int ]
		dll.PyLong_FromString.__doc__ = """Return value: New reference. Return a new PyLongObject based on the string value in str , which is
	interpreted according to the radix in base .  If pend is non- NULL , *pend will point to the first character in str which follows the
	representation of the number.  If base is 0 , the radix will be determined
	based on the leading characters of str : if str starts with '0x' or '0X' , radix 16 will be used; if str starts with '0' , radix 8 will be
	used; otherwise radix 10 will be used.  If base is not 0 , it must be
	between 2 and 36 , inclusive.  Leading spaces are ignored.  If there are
	no digits, ValueError will be raised."""
		dll.PyLong_FromUnicode.restype = POINTER(PyObject)
		dll.PyLong_FromUnicode.argtypes = [ c_wchar_p, c_ssize_t, c_int ]
		dll.PyLong_FromUnicode.__doc__ = """Return value: New reference. Convert a sequence of Unicode digits to a Python long integer value.  The first
	parameter, u , points to the first character of the Unicode string, length gives the number of characters, and base is the radix for the conversion.  The
	radix must be in the range [2, 36]; if it is out of range, ValueError will be raised. New in version 1.6. Changed in version 2.5: This function used an c_int for length . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll._PyLong_Sign.restype = c_int
		dll._PyLong_Sign.argtypes = [ POINTER(PyObject) ]
		dll._PyLong_NumBits.restype = c_size_t
		dll._PyLong_NumBits.argtypes = [ POINTER(PyObject) ]
		dll._PyLong_FromByteArray.restype = POINTER(PyObject)
		dll._PyLong_FromByteArray.argtypes = [ c_uchar_p, c_size_t, c_int, c_int ]
		dll._PyLong_AsByteArray.restype = c_int
		dll._PyLong_AsByteArray.argtypes = [ POINTER(py_object), c_uchar_p, c_size_t, c_int, c_int ]
		dll._PyLong_Format.restype = POINTER(PyObject)
		dll._PyLong_Format.argtypes = [ POINTER(PyObject), c_int, c_int, c_int ]
		dll._PyLong_FormatAdvanced.restype = POINTER(PyObject)
		dll._PyLong_FormatAdvanced.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t ]
		dll.PyFloat_GetMax.restype = c_double
		dll.PyFloat_GetMax.argtypes = [  ]
		dll.PyFloat_GetMax.__doc__ = """Return the maximum representable finite float DBL_MAX as C double . New in version 2.6."""
		dll.PyFloat_GetMin.restype = c_double
		dll.PyFloat_GetMin.argtypes = [  ]
		dll.PyFloat_GetMin.__doc__ = """Return the minimum normalized positive float DBL_MIN as C double . New in version 2.6."""
		dll.PyFloat_GetInfo.restype = POINTER(PyObject)
		dll.PyFloat_GetInfo.argtypes = [  ]
		dll.PyFloat_GetInfo.__doc__ = """Return a structseq instance which contains information about the
	precision, minimum and maximum values of a float. It's a thin wrapper
	around the header file float.h . New in version 2.6."""
		dll.PyFloat_FromString.restype = POINTER(PyObject)
		dll.PyFloat_FromString.argtypes = [ POINTER(PyObject), POINTER(c_char_p) ]
		dll.PyFloat_FromString.__doc__ = """Return value: New reference. Create a PyFloatObject object based on the string value in str , or NULL on failure.  The pend argument is ignored.  It remains only for
	backward compatibility."""
		dll.PyFloat_FromDouble.restype = POINTER(PyObject)
		dll.PyFloat_FromDouble.argtypes = [ c_double ]
		dll.PyFloat_FromDouble.__doc__ = """Return value: New reference. Create a PyFloatObject object from v , or NULL on failure."""
		dll.PyFloat_AsDouble.restype = c_double
		dll.PyFloat_AsDouble.argtypes = [ POINTER(PyObject) ]
		dll.PyFloat_AsDouble.__doc__ = """Return a C double representation of the contents of pyfloat .  If pyfloat is not a Python floating point object but has a __float__() method, this method will first be called to convert pyfloat into a float.
	This method returns -1.0 upon failure, so one should call PyErr_Occurred() to check for errors."""
		dll.PyFloat_AsReprString.restype = None
		dll.PyFloat_AsReprString.argtypes = [ c_char_p, POINTER(py_object) ]
		dll.PyFloat_AsReprString.__doc__ = """Same as PyFloat_AsString, except uses the same rules as repr() .  The length of buf should be at least 100. This function is unsafe to call because it writes to a buffer whose
	length it does not know. Deprecated since version 2.7: Use PyObject_Repr() or PyOS_double_to_string() instead."""
		dll.PyFloat_AsString.restype = None
		dll.PyFloat_AsString.argtypes = [ c_char_p, POINTER(py_object) ]
		dll.PyFloat_AsString.__doc__ = """Convert the argument v to a string, using the same rules as str() . The length of buf should be at least 100. This function is unsafe to call because it writes to a buffer whose
	length it does not know. Deprecated since version 2.7: Use PyObject_Str() or PyOS_double_to_string() instead."""
		dll._PyFloat_Pack4.restype = c_int
		dll._PyFloat_Pack4.argtypes = [ c_double, c_uchar_p, c_int ]
		dll._PyFloat_Pack8.restype = c_int
		dll._PyFloat_Pack8.argtypes = [ c_double, c_uchar_p, c_int ]
		dll._PyFloat_Digits.restype = c_int
		dll._PyFloat_Digits.argtypes = [ c_char_p, c_double, POINTER(c_int) ]
		dll._PyFloat_DigitsInit.restype = None
		dll._PyFloat_DigitsInit.argtypes = [  ]
		dll._PyFloat_Unpack4.restype = c_double
		dll._PyFloat_Unpack4.argtypes = [ c_uchar_p, c_int ]
		dll._PyFloat_Unpack8.restype = c_double
		dll._PyFloat_Unpack8.argtypes = [ c_uchar_p, c_int ]
		dll.PyFloat_ClearFreeList.restype = c_int
		dll.PyFloat_ClearFreeList.argtypes = [  ]
		dll.PyFloat_ClearFreeList.__doc__ = """Clear the float free list. Return the number of items that could not
	be freed. New in version 2.6."""
		dll._PyFloat_FormatAdvanced.restype = POINTER(PyObject)
		dll._PyFloat_FormatAdvanced.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t ]
		dll._Py_double_round.restype = POINTER(PyObject)
		dll._Py_double_round.argtypes = [ c_double, c_int ]
		dll._Py_c_sum.restype = py_object
		dll._Py_c_sum.argtypes = [ py_object, py_object ]
		dll._Py_c_sum.__doc__ = """Return the sum of two complex numbers, using the C Py_complex representation."""
		dll._Py_c_diff.restype = py_object
		dll._Py_c_diff.argtypes = [ py_object, py_object ]
		dll._Py_c_diff.__doc__ = """Return the difference between two complex numbers, using the C Py_complex representation."""
		dll._Py_c_neg.restype = py_object
		dll._Py_c_neg.argtypes = [ py_object ]
		dll._Py_c_neg.__doc__ = """Return the negation of the complex number complex , using the C Py_complex representation."""
		dll._Py_c_prod.restype = py_object
		dll._Py_c_prod.argtypes = [ py_object, py_object ]
		dll._Py_c_prod.__doc__ = """Return the product of two complex numbers, using the C Py_complex representation."""
		dll._Py_c_quot.restype = py_object
		dll._Py_c_quot.argtypes = [ py_object, py_object ]
		dll._Py_c_quot.__doc__ = """Return the quotient of two complex numbers, using the C Py_complex representation. If divisor is null, this method returns zero and sets errno to EDOM ."""
		dll._Py_c_pow.restype = py_object
		dll._Py_c_pow.argtypes = [ py_object, py_object ]
		dll._Py_c_pow.__doc__ = """Return the exponentiation of num by exp , using the C Py_complex representation. If num is null and exp is not a positive real number,
	this method returns zero and sets errno to EDOM ."""
		dll._Py_c_abs.restype = c_double
		dll._Py_c_abs.argtypes = [ py_object ]
		dll.PyComplex_FromCComplex.restype = POINTER(PyObject)
		dll.PyComplex_FromCComplex.argtypes = [ py_object ]
		dll.PyComplex_FromCComplex.__doc__ = """Return value: New reference. Create a new Python complex number object from a C Py_complex value."""
		dll.PyComplex_FromDoubles.restype = POINTER(PyObject)
		dll.PyComplex_FromDoubles.argtypes = [ c_double, c_double ]
		dll.PyComplex_FromDoubles.__doc__ = """Return value: New reference. Return a new PyComplexObject object from real and imag ."""
		dll.PyComplex_RealAsDouble.restype = c_double
		dll.PyComplex_RealAsDouble.argtypes = [ POINTER(PyObject) ]
		dll.PyComplex_RealAsDouble.__doc__ = """Return the real part of op as a C double ."""
		dll.PyComplex_ImagAsDouble.restype = c_double
		dll.PyComplex_ImagAsDouble.argtypes = [ POINTER(PyObject) ]
		dll.PyComplex_ImagAsDouble.__doc__ = """Return the imaginary part of op as a C double ."""
		dll.PyComplex_AsCComplex.restype = py_object
		dll.PyComplex_AsCComplex.argtypes = [ POINTER(PyObject) ]
		dll.PyComplex_AsCComplex.__doc__ = """Return the Py_complex value of the complex number op .
	Upon failure, this method returns -1.0 as a real value. Changed in version 2.6: If op is not a Python complex number object but has a __complex__() method, this method will first be called to convert op to a Python complex
	number object."""
		dll._PyComplex_FormatAdvanced.restype = POINTER(PyObject)
		dll._PyComplex_FormatAdvanced.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t ]
		dll.PyString_FromStringAndSize.restype = POINTER(PyObject)
		dll.PyString_FromStringAndSize.argtypes = [ c_char_p, c_ssize_t ]
		dll.PyString_FromStringAndSize.__doc__ = """Return value: New reference. Return a new string object with a copy of the string v as value and length len on success, and NULL on failure.  If v is NULL , the contents of the
	string are uninitialized. Changed in version 2.5: This function used an c_int type for len . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyString_FromString.restype = POINTER(PyObject)
		dll.PyString_FromString.argtypes = [ c_char_p ]
		dll.PyString_FromString.__doc__ = """Return value: New reference. Return a new string object with a copy of the string v as value on success,
	and NULL on failure.  The parameter v must not be NULL ; it will not be
	checked."""
		dll.PyString_FromFormatV.restype = POINTER(PyObject)
		dll.PyString_FromFormatV.argtypes = [ c_char_p, va_list ]
		dll.PyString_FromFormatV.__doc__ = """Return value: New reference. Identical to PyString_FromFormat() except that it takes exactly two
	arguments."""
		dll.PyString_FromFormat.restype = POINTER(PyObject)
		dll.PyString_FromFormat.argtypes = [ c_char_p, va_list ]
		dll.PyString_FromFormat.__doc__ = """Return value: New reference. Take a C printf() -style format string and a variable number of
	arguments, calculate the size of the resulting Python string and return a string
	with the values formatted into it.  The variable arguments must be C types and
	must correspond exactly to the format characters in the format string.  The
	following format characters are allowed: Format Characters Type Comment %% n/a The literal % character. %c c_int A single character,
	represented as an C c_int. %d c_int Exactly equivalent to printf("%d") . %u unsigned c_int Exactly equivalent to printf("%u") . %ld long Exactly equivalent to printf("%ld") . %lu unsigned long Exactly equivalent to printf("%lu") . %lld long long Exactly equivalent to printf("%lld") . %llu unsigned
	long long Exactly equivalent to printf("%llu") . %zd Py_ssize_t Exactly equivalent to printf("%zd") . %zu size_t Exactly equivalent to printf("%zu") . %i c_int Exactly equivalent to printf("%i") . %x c_int Exactly equivalent to printf("%x") . %s char* A null-terminated C character
	array. %p void* The hex representation of a C
	pointer. Mostly equivalent to printf("%p") except that
	it is guaranteed to start with
	the literal 0x regardless
	of what the platform's printf yields. An unrecognized format character causes all the rest of the format string to be
	copied as-is to the result string, and any extra arguments discarded. Note The "%lld" and "%llu" format specifiers are only available
	when HAVE_LONG_LONG is defined. Changed in version 2.7: Support for "%lld" and "%llu" added."""
		dll.PyString_Size.restype = c_ssize_t
		dll.PyString_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyString_Size.__doc__ = """Return the length of the string in string object string . Changed in version 2.5: This function returned an c_int type. This might require changes
	in your code for properly supporting 64-bit systems."""
		dll.PyString_AsString.restype = c_char_p
		dll.PyString_AsString.argtypes = [ POINTER(PyObject) ]
		dll.PyString_AsString.__doc__ = """Return a NUL-terminated representation of the contents of string .  The pointer
	refers to the internal buffer of string , not a copy.  The data must not be
	modified in any way, unless the string was just created using PyString_FromStringAndSize(NULL, size) . It must not be deallocated.  If string is a Unicode object, this function computes the default encoding of string and operates on that.  If string is not a string object at all, PyString_AsString() returns NULL and raises TypeError ."""
		dll.PyString_Repr.restype = POINTER(PyObject)
		dll.PyString_Repr.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyString_Concat.restype = None
		dll.PyString_Concat.argtypes = [ POINTER(POINTER(PyObject)), POINTER(PyObject) ]
		dll.PyString_Concat.__doc__ = """Create a new string object in *string containing the contents of newpart appended to string ; the caller will own the new reference.  The reference to
	the old value of string will be stolen.  If the new string cannot be created,
	the old reference to string will still be discarded and the value of *string will be set to NULL ; the appropriate exception will be set."""
		dll.PyString_ConcatAndDel.restype = None
		dll.PyString_ConcatAndDel.argtypes = [ POINTER(POINTER(PyObject)), POINTER(PyObject) ]
		dll.PyString_ConcatAndDel.__doc__ = """Create a new string object in *string containing the contents of newpart appended to string .  This version decrements the reference count of newpart ."""
		dll._PyString_Resize.restype = c_int
		dll._PyString_Resize.argtypes = [ POINTER(POINTER(PyObject)), c_ssize_t ]
		dll._PyString_Resize.__doc__ = """A way to resize a string object even though it is "immutable". Only use this to
	build up a brand new string object; don't use this if the string may already be
	known in other parts of the code.  It is an error to call this function if the
	refcount on the input string object is not one. Pass the address of an existing
	string object as an lvalue (it may be written into), and the new size desired.
	On success, *string holds the resized string object and 0 is returned;
	the address in *string may differ from its input value.  If the reallocation
	fails, the original string object at *string is deallocated, *string is
	set to NULL , a memory exception is set, and -1 is returned. Changed in version 2.5: This function used an c_int type for newsize . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll._PyString_Eq.restype = c_int
		dll._PyString_Eq.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyString_Format.restype = POINTER(PyObject)
		dll.PyString_Format.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyString_Format.__doc__ = """Return value: New reference. Return a new string object from format and args . Analogous to format % args .  The args argument must be a tuple."""
		dll._PyString_FormatLong.restype = POINTER(PyObject)
		dll._PyString_FormatLong.argtypes = [ POINTER(PyObject), c_int, c_int, c_int, POINTER(c_char_p), POINTER(c_int) ]
		dll.PyString_DecodeEscape.restype = POINTER(PyObject)
		dll.PyString_DecodeEscape.argtypes = [ c_char_p, c_ssize_t, c_char_p, c_ssize_t, c_char_p ]
		dll.PyString_InternInPlace.restype = None
		dll.PyString_InternInPlace.argtypes = [ POINTER(POINTER(PyObject)) ]
		dll.PyString_InternInPlace.__doc__ = """Intern the argument *string in place.  The argument must be the address of a
	pointer variable pointing to a Python string object.  If there is an existing
	interned string that is the same as *string , it sets *string to it
	(decrementing the reference count of the old string object and incrementing the
	reference count of the interned string object), otherwise it leaves *string alone and interns it (incrementing its reference count).  (Clarification: even
	though there is a lot of talk about reference counts, think of this function as
	reference-count-neutral; you own the object after the call if and only if you
	owned it before the call.) Note This function is not available in 3.x and does not have a PyBytes alias."""
		dll.PyString_InternImmortal.restype = None
		dll.PyString_InternImmortal.argtypes = [ POINTER(POINTER(PyObject)) ]
		dll.PyString_InternFromString.restype = POINTER(PyObject)
		dll.PyString_InternFromString.argtypes = [ c_char_p ]
		dll.PyString_InternFromString.__doc__ = """Return value: New reference. A combination of PyString_FromString() and PyString_InternInPlace() , returning either a new string object that has
	been interned, or a new ("owned") reference to an earlier interned string object
	with the same value. Note This function is not available in 3.x and does not have a PyBytes alias."""
		dll._Py_ReleaseInternedStrings.restype = None
		dll._Py_ReleaseInternedStrings.argtypes = [  ]
		dll._PyString_Join.restype = POINTER(PyObject)
		dll._PyString_Join.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyString_Decode.restype = POINTER(PyObject)
		dll.PyString_Decode.argtypes = [ c_char_p, c_ssize_t, c_char_p, c_char_p ]
		dll.PyString_Decode.__doc__ = """Return value: New reference. Create an object by decoding size bytes of the encoded buffer s using the
	codec registered for encoding . encoding and errors have the same meaning
	as the parameters of the same name in the unicode() built-in function.
	The codec to be used is looked up using the Python codec registry.  Return NULL if an exception was raised by the codec. Note This function is not available in 3.x and does not have a PyBytes alias. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyString_Encode.restype = POINTER(PyObject)
		dll.PyString_Encode.argtypes = [ c_char_p, c_ssize_t, c_char_p, c_char_p ]
		dll.PyString_Encode.__doc__ = """Return value: New reference. Encode the char buffer of the given size by passing it to the codec
	registered for encoding and return a Python object. encoding and errors have the same meaning as the parameters of the same name in the string encode() method. The codec to be used is looked up using the Python codec
	registry.  Return NULL if an exception was raised by the codec. Note This function is not available in 3.x and does not have a PyBytes alias. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyString_AsEncodedObject.restype = POINTER(PyObject)
		dll.PyString_AsEncodedObject.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyString_AsEncodedObject.__doc__ = """Return value: New reference. Encode a string object using the codec registered for encoding and return the
	result as Python object. encoding and errors have the same meaning as the
	parameters of the same name in the string encode() method. The codec to be
	used is looked up using the Python codec registry. Return NULL if an exception
	was raised by the codec. Note This function is not available in 3.x and does not have a PyBytes alias."""
		dll.PyString_AsEncodedString.restype = POINTER(PyObject)
		dll.PyString_AsEncodedString.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyString_AsDecodedObject.restype = POINTER(PyObject)
		dll.PyString_AsDecodedObject.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyString_AsDecodedObject.__doc__ = """Return value: New reference. Decode a string object by passing it to the codec registered for encoding and
	return the result as Python object. encoding and errors have the same
	meaning as the parameters of the same name in the string encode() method.
	The codec to be used is looked up using the Python codec registry. Return NULL if an exception was raised by the codec. Note This function is not available in 3.x and does not have a PyBytes alias."""
		dll.PyString_AsDecodedString.restype = POINTER(PyObject)
		dll.PyString_AsDecodedString.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyString_AsStringAndSize.restype = c_int
		dll.PyString_AsStringAndSize.argtypes = [ POINTER(PyObject), POINTER(c_char_p), POINTER(c_ssize_t) ]
		dll.PyString_AsStringAndSize.__doc__ = """Return a NUL-terminated representation of the contents of the object obj through the output variables buffer and length . The function accepts both string and Unicode objects as input. For Unicode
	objects it returns the default encoded version of the object.  If length is NULL , the resulting buffer may not contain NUL characters; if it does, the
	function returns -1 and a TypeError is raised. The buffer refers to an internal string buffer of obj , not a copy. The data
	must not be modified in any way, unless the string was just created using PyString_FromStringAndSize(NULL, size) .  It must not be deallocated.  If string is a Unicode object, this function computes the default encoding of string and operates on that.  If string is not a string object at all, PyString_AsStringAndSize() returns -1 and raises TypeError . Changed in version 2.5: This function used an c_int * type for length . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll._PyString_InsertThousandsGroupingLocale.restype = c_ssize_t
		dll._PyString_InsertThousandsGroupingLocale.argtypes = [ c_char_p, c_ssize_t, c_char_p, c_ssize_t, c_ssize_t ]
		dll._PyString_InsertThousandsGrouping.restype = c_ssize_t
		dll._PyString_InsertThousandsGrouping.argtypes = [ c_char_p, c_ssize_t, c_char_p, c_ssize_t, c_ssize_t, c_char_p, c_char_p ]
		dll._PyBytes_FormatAdvanced.restype = POINTER(PyObject)
		dll._PyBytes_FormatAdvanced.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t ]
		dll.PyMemoryView_GetContiguous.restype = POINTER(PyObject)
		dll.PyMemoryView_GetContiguous.argtypes = [ POINTER(PyObject), c_int, c_char ]
		dll.PyMemoryView_GetContiguous.__doc__ = """Create a memoryview object to a contiguous chunk of memory (in either
	'C' or 'F'ortran order ) from an object that defines the buffer
	interface. If memory is contiguous, the memoryview object points to the
	original memory. Otherwise copy is made and the memoryview points to a
	new bytes object."""
		dll.PyMemoryView_FromObject.restype = POINTER(PyObject)
		dll.PyMemoryView_FromObject.argtypes = [ POINTER(PyObject) ]
		dll.PyMemoryView_FromObject.__doc__ = """Create a memoryview object from an object that defines the new buffer
	interface."""
		dll.PyMemoryView_FromBuffer.restype = POINTER(PyObject)
		dll.PyMemoryView_FromBuffer.argtypes = [ POINTER(py_object) ]
		dll.PyMemoryView_FromBuffer.__doc__ = """Create a memoryview object wrapping the given buffer-info structure view .
	The memoryview object then owns the buffer, which means you shouldn't
	try to release it yourself: it will be released on deallocation of the
	memoryview object."""
		dll.PyBuffer_FromObject.restype = POINTER(PyObject)
		dll.PyBuffer_FromObject.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PyBuffer_FromObject.__doc__ = """Return value: New reference. Return a new read-only buffer object.  This raises TypeError if base doesn't support the read-only buffer protocol or doesn't provide
	exactly one buffer segment, or it raises ValueError if offset is
	less than zero.  The buffer will hold a reference to the base object, and
	the buffer's contents will refer to the base object's buffer interface,
	starting as position offset and extending for size bytes. If size is Py_END_OF_BUFFER , then the new buffer's contents extend to the
	length of the base object's exported buffer data. Changed in version 2.5: This function used an c_int type for offset and size . This
	might require changes in your code for properly supporting 64-bit
	systems."""
		dll.PyBuffer_FromReadWriteObject.restype = POINTER(PyObject)
		dll.PyBuffer_FromReadWriteObject.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PyBuffer_FromReadWriteObject.__doc__ = """Return value: New reference. Return a new writable buffer object.  Parameters and exceptions are similar
	to those for PyBuffer_FromObject() .  If the base object does not
	export the writeable buffer protocol, then TypeError is raised. Changed in version 2.5: This function used an c_int type for offset and size . This
	might require changes in your code for properly supporting 64-bit
	systems."""
		dll.PyBuffer_FromMemory.restype = POINTER(PyObject)
		dll.PyBuffer_FromMemory.argtypes = [ c_void_p, c_ssize_t ]
		dll.PyBuffer_FromMemory.__doc__ = """Return value: New reference. Return a new read-only buffer object that reads from a specified location
	in memory, with a specified size.  The caller is responsible for ensuring
	that the memory buffer, passed in as ptr , is not deallocated while the
	returned buffer object exists.  Raises ValueError if size is less
	than zero.  Note that Py_END_OF_BUFFER may not be passed for the size parameter; ValueError will be raised in that case. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyBuffer_FromReadWriteMemory.restype = POINTER(PyObject)
		dll.PyBuffer_FromReadWriteMemory.argtypes = [ c_void_p, c_ssize_t ]
		dll.PyBuffer_FromReadWriteMemory.__doc__ = """Return value: New reference. Similar to PyBuffer_FromMemory() , but the returned buffer is
	writable. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyBuffer_New.restype = POINTER(PyObject)
		dll.PyBuffer_New.argtypes = [ c_ssize_t ]
		dll.PyBuffer_New.__doc__ = """Return value: New reference. Return a new writable buffer object that maintains its own memory buffer of size bytes. ValueError is returned if size is not zero or
	positive.  Note that the memory buffer (as returned by PyObject_AsWriteBuffer() ) is not specifically aligned. Changed in version 2.5: This function used an c_int type for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyByteArray_FromObject.restype = POINTER(PyObject)
		dll.PyByteArray_FromObject.argtypes = [ POINTER(PyObject) ]
		dll.PyByteArray_FromObject.__doc__ = """Return a new bytearray object from any object, o , that implements the
	buffer protocol."""
		dll.PyByteArray_Concat.restype = POINTER(PyObject)
		dll.PyByteArray_Concat.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyByteArray_Concat.__doc__ = """Concat bytearrays a and b and return a new bytearray with the result."""
		dll.PyByteArray_FromStringAndSize.restype = POINTER(PyObject)
		dll.PyByteArray_FromStringAndSize.argtypes = [ c_char_p, c_ssize_t ]
		dll.PyByteArray_FromStringAndSize.__doc__ = """Create a new bytearray object from string and its length, len .  On
	failure, NULL is returned."""
		dll.PyByteArray_Size.restype = c_ssize_t
		dll.PyByteArray_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyByteArray_Size.__doc__ = """Return the size of bytearray after checking for a NULL pointer."""
		dll.PyByteArray_AsString.restype = c_char_p
		dll.PyByteArray_AsString.argtypes = [ POINTER(PyObject) ]
		dll.PyByteArray_AsString.__doc__ = """Return the contents of bytearray as a char array after checking for a NULL pointer."""
		dll.PyByteArray_Resize.restype = c_int
		dll.PyByteArray_Resize.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyByteArray_Resize.__doc__ = """Resize the internal buffer of bytearray to len ."""
		dll.PyTuple_New.restype = POINTER(PyObject)
		dll.PyTuple_New.argtypes = [ c_ssize_t ]
		dll.PyTuple_New.__doc__ = """Return value: New reference. Return a new tuple object of size len , or NULL on failure. Changed in version 2.5: This function used an c_int type for len . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyTuple_Size.restype = c_ssize_t
		dll.PyTuple_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyTuple_Size.__doc__ = """Take a pointer to a tuple object, and return the size of that tuple. Changed in version 2.5: This function returned an c_int type. This might require changes
	in your code for properly supporting 64-bit systems."""
		dll.PyTuple_GetItem.restype = POINTER(PyObject)
		dll.PyTuple_GetItem.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyTuple_GetItem.__doc__ = """Return value: Borrowed reference. Return the object at position pos in the tuple pointed to by p .  If pos is
	out of bounds, return NULL and sets an IndexError exception. Changed in version 2.5: This function used an c_int type for pos . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyTuple_SetItem.restype = c_int
		dll.PyTuple_SetItem.argtypes = [ POINTER(PyObject), c_ssize_t, POINTER(PyObject) ]
		dll.PyTuple_SetItem.__doc__ = """Insert a reference to object o at position pos of the tuple pointed to by p . Return 0 on success. Note This function "steals" a reference to o . Changed in version 2.5: This function used an c_int type for pos . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyTuple_GetSlice.restype = POINTER(PyObject)
		dll.PyTuple_GetSlice.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PyTuple_GetSlice.__doc__ = """Return value: New reference. Take a slice of the tuple pointed to by p from low to high and return it
	as a new tuple. Changed in version 2.5: This function used an c_int type for low and high . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll._PyTuple_Resize.restype = c_int
		dll._PyTuple_Resize.argtypes = [ POINTER(POINTER(PyObject)), c_ssize_t ]
		dll._PyTuple_Resize.__doc__ = """Can be used to resize a tuple. newsize will be the new length of the tuple.
	Because tuples are supposed to be immutable, this should only be used if there
	is only one reference to the object.  Do not use this if the tuple may already
	be known to some other part of the code.  The tuple will always grow or shrink
	at the end.  Think of this as destroying the old tuple and creating a new one,
	only more efficiently.  Returns 0 on success. Client code should never
	assume that the resulting value of *p will be the same as before calling
	this function. If the object referenced by *p is replaced, the original *p is destroyed.  On failure, returns -1 and sets *p to NULL , and
	raises MemoryError or SystemError . Changed in version 2.2: Removed unused third parameter, last_is_sticky . Changed in version 2.5: This function used an c_int type for newsize . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PyTuple_Pack.restype = POINTER(PyObject)
		dll.PyTuple_Pack.argtypes = [ c_ssize_t, va_list ]
		dll.PyTuple_Pack.__doc__ = """Return value: New reference. Return a new tuple object of size n , or NULL on failure. The tuple values
	are initialized to the subsequent n C arguments pointing to Python objects. PyTuple_Pack(2, a, b) is equivalent to Py_BuildValue("(OO)", a, b) . New in version 2.4. Changed in version 2.5: This function used an c_int type for n . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll._PyTuple_MaybeUntrack.restype = None
		dll._PyTuple_MaybeUntrack.argtypes = [ POINTER(PyObject) ]
		dll.PyTuple_ClearFreeList.restype = c_int
		dll.PyTuple_ClearFreeList.argtypes = [  ]
		dll.PyTuple_ClearFreeList.__doc__ = """Clear the free list. Return the total number of freed items. New in version 2.6."""
		dll.PyList_New.restype = POINTER(PyObject)
		dll.PyList_New.argtypes = [ c_ssize_t ]
		dll.PyList_New.__doc__ = """Return value: New reference. Return a new list of length len on success, or NULL on failure. Note If len is greater than zero, the returned list object's items are
	set to NULL .  Thus you cannot use abstract API functions such as PySequence_SetItem() or expose the object to Python code before
	setting all items to a real object with PyList_SetItem() . Changed in version 2.5: This function used an c_int for size . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyList_Size.restype = c_ssize_t
		dll.PyList_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyList_Size.__doc__ = """Return the length of the list object in list ; this is equivalent to len(list) on a list object. Changed in version 2.5: This function returned an c_int . This might require changes in
	your code for properly supporting 64-bit systems."""
		dll.PyList_GetItem.restype = POINTER(PyObject)
		dll.PyList_GetItem.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyList_GetItem.__doc__ = """Return value: Borrowed reference. Return the object at position index in the list pointed to by list .  The
	position must be positive, indexing from the end of the list is not
	supported.  If index is out of bounds, return NULL and set an IndexError exception. Changed in version 2.5: This function used an c_int for index . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyList_SetItem.restype = c_int
		dll.PyList_SetItem.argtypes = [ POINTER(PyObject), c_ssize_t, POINTER(PyObject) ]
		dll.PyList_SetItem.__doc__ = """Set the item at index index in list to item .  Return 0 on success
	or -1 on failure. Note This function "steals" a reference to item and discards a reference to
	an item already in the list at the affected position. Changed in version 2.5: This function used an c_int for index . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyList_Insert.restype = c_int
		dll.PyList_Insert.argtypes = [ POINTER(PyObject), c_ssize_t, POINTER(PyObject) ]
		dll.PyList_Insert.__doc__ = """Insert the item item into list list in front of index index .  Return 0 if successful; return -1 and set an exception if unsuccessful.
	Analogous to list.insert(index, item) . Changed in version 2.5: This function used an c_int for index . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyList_Append.restype = c_int
		dll.PyList_Append.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyList_Append.__doc__ = """Append the object item at the end of list list . Return 0 if
	successful; return -1 and set an exception if unsuccessful.  Analogous
	to list.append(item) ."""
		dll.PyList_GetSlice.restype = POINTER(PyObject)
		dll.PyList_GetSlice.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PyList_GetSlice.__doc__ = """Return value: New reference. Return a list of the objects in list containing the objects between low and high .  Return NULL and set an exception if unsuccessful.  Analogous
	to list[low:high] .  Negative indices, as when slicing from Python, are not
	supported. Changed in version 2.5: This function used an c_int for low and high . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PyList_SetSlice.restype = c_int
		dll.PyList_SetSlice.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t, POINTER(PyObject) ]
		dll.PyList_SetSlice.__doc__ = """Set the slice of list between low and high to the contents of itemlist .  Analogous to list[low:high] = itemlist . The itemlist may
	be NULL , indicating the assignment of an empty list (slice deletion).
	Return 0 on success, -1 on failure.  Negative indices, as when
	slicing from Python, are not supported. Changed in version 2.5: This function used an c_int for low and high . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PyList_Sort.restype = c_int
		dll.PyList_Sort.argtypes = [ POINTER(PyObject) ]
		dll.PyList_Sort.__doc__ = """Sort the items of list in place.  Return 0 on success, -1 on
	failure.  This is equivalent to list.sort() ."""
		dll.PyList_Reverse.restype = c_int
		dll.PyList_Reverse.argtypes = [ POINTER(PyObject) ]
		dll.PyList_Reverse.__doc__ = """Reverse the items of list in place.  Return 0 on success, -1 on
	failure.  This is the equivalent of list.reverse() ."""
		dll.PyList_AsTuple.restype = POINTER(PyObject)
		dll.PyList_AsTuple.argtypes = [ POINTER(PyObject) ]
		dll.PyList_AsTuple.__doc__ = """Return value: New reference. Return a new tuple object containing the contents of list ; equivalent to tuple(list) ."""
		dll._PyList_Extend.restype = POINTER(PyObject)
		dll._PyList_Extend.argtypes = [ POINTER(py_object), POINTER(PyObject) ]
		dll.PyDict_New.restype = POINTER(PyObject)
		dll.PyDict_New.argtypes = [  ]
		dll.PyDict_New.__doc__ = """Return value: New reference. Return a new empty dictionary, or NULL on failure."""
		dll.PyDict_GetItem.restype = POINTER(PyObject)
		dll.PyDict_GetItem.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyDict_GetItem.__doc__ = """Return value: Borrowed reference. Return the object from dictionary p which has a key key .  Return NULL if the key key is not present, but without setting an exception."""
		dll.PyDict_SetItem.restype = c_int
		dll.PyDict_SetItem.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyDict_SetItem.__doc__ = """Insert value into the dictionary p with a key of key . key must be hashable ; if it isn't, TypeError will be raised. Return 0 on success or -1 on failure."""
		dll.PyDict_DelItem.restype = c_int
		dll.PyDict_DelItem.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyDict_DelItem.__doc__ = """Remove the entry in dictionary p with key key . key must be hashable;
	if it isn't, TypeError is raised.  Return 0 on success or -1 on failure."""
		dll.PyDict_Clear.restype = None
		dll.PyDict_Clear.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Clear.__doc__ = """Empty an existing dictionary of all key-value pairs."""
		dll.PyDict_Next.restype = c_int
		dll.PyDict_Next.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t), POINTER(POINTER(PyObject)), POINTER(POINTER(PyObject)) ]
		dll.PyDict_Next.__doc__ = """Iterate over all key-value pairs in the dictionary p .  The Py_ssize_t referred to by ppos must be initialized to 0 prior to the first call to this function to start the iteration; the
	function returns true for each pair in the dictionary, and false once all
	pairs have been reported.  The parameters pkey and pvalue should either
	point to PyObject* variables that will be filled in with each key
	and value, respectively, or may be NULL .  Any references returned through
	them are borrowed. ppos should not be altered during iteration. Its
	value represents offsets within the internal dictionary structure, and
	since the structure is sparse, the offsets are not consecutive. For example: PyObject * key , * value ; Py_ssize_t pos = 0 ; while ( PyDict_Next ( self -> dict , & pos , & key , & value )) { /* do something interesting with the values... */ ... } The dictionary p should not be mutated during iteration.  It is safe
	(since Python 2.1) to modify the values of the keys as you iterate over the
	dictionary, but only so long as the set of keys does not change.  For
	example: PyObject * key , * value ; Py_ssize_t pos = 0 ; while ( PyDict_Next ( self -> dict , & pos , & key , & value )) { c_int i = PyInt_AS_LONG ( value ) + 1 ; PyObject * o = PyInt_FromLong ( i ); if ( o == NULL ) return - 1 ; if ( PyDict_SetItem ( self -> dict , key , o ) < 0 ) { Py_DECREF ( o ); return - 1 ; } Py_DECREF ( o ); } Changed in version 2.5: This function used an c_int * type for ppos . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll._PyDict_Next.restype = c_int
		dll._PyDict_Next.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t), POINTER(POINTER(PyObject)), POINTER(POINTER(PyObject)), POINTER(long) ]
		dll.PyDict_Keys.restype = POINTER(PyObject)
		dll.PyDict_Keys.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Keys.__doc__ = """Return value: New reference. Return a PyListObject containing all the keys from the dictionary,
	as in the dictionary method dict.keys() ."""
		dll.PyDict_Values.restype = POINTER(PyObject)
		dll.PyDict_Values.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Values.__doc__ = """Return value: New reference. Return a PyListObject containing all the values from the
	dictionary p , as in the dictionary method dict.values() ."""
		dll.PyDict_Items.restype = POINTER(PyObject)
		dll.PyDict_Items.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Items.__doc__ = """Return value: New reference. Return a PyListObject containing all the items from the
	dictionary, as in the dictionary method dict.items() ."""
		dll.PyDict_Size.restype = c_ssize_t
		dll.PyDict_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Size.__doc__ = """Return the number of items in the dictionary.  This is equivalent to len(p) on a dictionary. Changed in version 2.5: This function returned an c_int type.  This might require changes
	in your code for properly supporting 64-bit systems."""
		dll.PyDict_Copy.restype = POINTER(PyObject)
		dll.PyDict_Copy.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Copy.__doc__ = """Return value: New reference. Return a new dictionary that contains the same key-value pairs as p . New in version 1.6."""
		dll.PyDict_Contains.restype = c_int
		dll.PyDict_Contains.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyDict_Contains.__doc__ = """Determine if dictionary p contains key .  If an item in p is matches key , return 1 , otherwise return 0 .  On error, return -1 .
	This is equivalent to the Python expression key in p . New in version 2.4."""
		dll._PyDict_Contains.restype = c_int
		dll._PyDict_Contains.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_long ]
		dll._PyDict_NewPresized.restype = POINTER(PyObject)
		dll._PyDict_NewPresized.argtypes = [ c_ssize_t ]
		dll._PyDict_MaybeUntrack.restype = None
		dll._PyDict_MaybeUntrack.argtypes = [ POINTER(PyObject) ]
		dll.PyDict_Update.restype = c_int
		dll.PyDict_Update.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyDict_Update.__doc__ = """This is the same as PyDict_Merge(a, b, 1) in C, or a.update(b) in
	Python.  Return 0 on success or -1 if an exception was raised. New in version 2.2."""
		dll.PyDict_Merge.restype = c_int
		dll.PyDict_Merge.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_int ]
		dll.PyDict_Merge.__doc__ = """Iterate over mapping object b adding key-value pairs to dictionary a . b may be a dictionary, or any object supporting PyMapping_Keys() and PyObject_GetItem() . If override is true, existing pairs in a will be replaced if a matching key is found in b , otherwise pairs will
	only be added if there is not a matching key in a . Return 0 on
	success or -1 if an exception was raised. New in version 2.2."""
		dll.PyDict_MergeFromSeq2.restype = c_int
		dll.PyDict_MergeFromSeq2.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_int ]
		dll.PyDict_MergeFromSeq2.__doc__ = """Update or merge into dictionary a , from the key-value pairs in seq2 . seq2 must be an iterable object producing iterable objects of length 2,
	viewed as key-value pairs.  In case of duplicate keys, the last wins if override is true, else the first wins. Return 0 on success or -1 if an exception was raised. Equivalent Python (except for the return
	value): def PyDict_MergeFromSeq2 ( a , seq2 , override ) : for key , value in seq2 : if override or key not in a : a [ key ] = value New in version 2.2."""
		dll.PyDict_GetItemString.restype = POINTER(PyObject)
		dll.PyDict_GetItemString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyDict_GetItemString.__doc__ = """Return value: Borrowed reference. This is the same as PyDict_GetItem() , but key is specified as a char* , rather than a PyObject* ."""
		dll.PyDict_SetItemString.restype = c_int
		dll.PyDict_SetItemString.argtypes = [ POINTER(PyObject), c_char_p, POINTER(PyObject) ]
		dll.PyDict_SetItemString.__doc__ = """Insert value into the dictionary p using key as a key. key should
	be a char* .  The key object is created using PyString_FromString(key) .  Return 0 on success or -1 on
	failure."""
		dll.PyDict_DelItemString.restype = c_int
		dll.PyDict_DelItemString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyDict_DelItemString.__doc__ = """Remove the entry in dictionary p which has a key specified by the string key .  Return 0 on success or -1 on failure."""
		dll.PySet_New.restype = POINTER(PyObject)
		dll.PySet_New.argtypes = [ POINTER(PyObject) ]
		dll.PySet_New.__doc__ = """Return value: New reference. Return a new set containing objects returned by the iterable .  The iterable may be NULL to create a new empty set.  Return the new set on
	success or NULL on failure.  Raise TypeError if iterable is not
	actually iterable.  The constructor is also useful for copying a set
	( c=set(s) )."""
		dll.PyFrozenSet_New.restype = POINTER(PyObject)
		dll.PyFrozenSet_New.argtypes = [ POINTER(PyObject) ]
		dll.PyFrozenSet_New.__doc__ = """Return value: New reference. Return a new frozenset containing objects returned by the iterable .
	The iterable may be NULL to create a new empty frozenset.  Return the new
	set on success or NULL on failure.  Raise TypeError if iterable is
	not actually iterable. Changed in version 2.6: Now guaranteed to return a brand-new frozenset .  Formerly,
	frozensets of zero-length were a singleton.  This got in the way of
	building-up new frozensets with PySet_Add() ."""
		dll.PySet_Size.restype = c_ssize_t
		dll.PySet_Size.argtypes = [ POINTER(PyObject) ]
		dll.PySet_Size.__doc__ = """Return the length of a set or frozenset object. Equivalent to len(anyset) .  Raises a PyExc_SystemError if anyset is not a set , frozenset , or an instance of a subtype. Changed in version 2.5: This function returned an c_int . This might require changes in
	your code for properly supporting 64-bit systems."""
		dll.PySet_Clear.restype = c_int
		dll.PySet_Clear.argtypes = [ POINTER(PyObject) ]
		dll.PySet_Clear.__doc__ = """Empty an existing set of all elements."""
		dll.PySet_Contains.restype = c_int
		dll.PySet_Contains.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySet_Contains.__doc__ = """Return 1 if found, 0 if not found, and -1 if an error is encountered.  Unlike
	the Python __contains__() method, this function does not automatically
	convert unhashable sets into temporary frozensets.  Raise a TypeError if
	the key is unhashable. Raise PyExc_SystemError if anyset is not a set , frozenset , or an instance of a subtype."""
		dll.PySet_Discard.restype = c_int
		dll.PySet_Discard.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySet_Discard.__doc__ = """Return 1 if found and removed, 0 if not found (no action taken), and -1 if an
	error is encountered.  Does not raise KeyError for missing keys.  Raise a TypeError if the key is unhashable.  Unlike the Python discard() method, this function does not automatically convert unhashable sets into
	temporary frozensets. Raise PyExc_SystemError if set is an not an
	instance of set or its subtype."""
		dll.PySet_Add.restype = c_int
		dll.PySet_Add.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySet_Add.__doc__ = """Add key to a set instance.  Does not apply to frozenset instances.  Return 0 on success or -1 on failure. Raise a TypeError if
	the key is unhashable. Raise a MemoryError if there is no room to grow.
	Raise a SystemError if set is an not an instance of set or its
	subtype. Changed in version 2.6: Now works with instances of frozenset or its subtypes.
	Like PyTuple_SetItem() in that it can be used to fill-in the
	values of brand new frozensets before they are exposed to other code."""
		dll._PySet_Next.restype = c_int
		dll._PySet_Next.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t), POINTER(POINTER(PyObject)) ]
		dll._PySet_NextEntry.restype = c_int
		dll._PySet_NextEntry.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t), POINTER(POINTER(PyObject)), POINTER(long) ]
		dll.PySet_Pop.restype = POINTER(PyObject)
		dll.PySet_Pop.argtypes = [ POINTER(PyObject) ]
		dll.PySet_Pop.__doc__ = """Return value: New reference. Return a new reference to an arbitrary object in the set , and removes the
	object from the set .  Return NULL on failure.  Raise KeyError if the
	set is empty. Raise a SystemError if set is an not an instance of set or its subtype."""
		dll._PySet_Update.restype = c_int
		dll._PySet_Update.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyCFunction_GetFunction.restype = py_object
		dll.PyCFunction_GetFunction.argtypes = [ POINTER(PyObject) ]
		dll.PyCFunction_GetSelf.restype = POINTER(PyObject)
		dll.PyCFunction_GetSelf.argtypes = [ POINTER(PyObject) ]
		dll.PyCFunction_GetFlags.restype = c_int
		dll.PyCFunction_GetFlags.argtypes = [ POINTER(PyObject) ]
		dll.PyCFunction_Call.restype = POINTER(PyObject)
		dll.PyCFunction_Call.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.Py_FindMethod.restype = POINTER(PyObject)
		dll.Py_FindMethod.argtypes = [ py_object, POINTER(PyObject), c_char_p ]
		dll.Py_FindMethod.__doc__ = """Return value: New reference. Return a bound method object for an extension type implemented in C.  This
	can be useful in the implementation of a tp_getattro or tp_getattr handler that does not use the PyObject_GenericGetAttr() function."""
		dll.PyCFunction_NewEx.restype = POINTER(PyObject)
		dll.PyCFunction_NewEx.argtypes = [ POINTER(py_object), POINTER(PyObject), POINTER(PyObject) ]
		dll.Py_FindMethodInChain.restype = POINTER(PyObject)
		dll.Py_FindMethodInChain.argtypes = [ POINTER(py_object), POINTER(PyObject), c_char_p ]
		dll.PyCFunction_ClearFreeList.restype = c_int
		dll.PyCFunction_ClearFreeList.argtypes = [  ]
		dll.PyModule_New.restype = POINTER(PyObject)
		dll.PyModule_New.argtypes = [ c_char_p ]
		dll.PyModule_New.__doc__ = """Return value: New reference. Return a new module object with the __name__ attribute set to name .
	Only the module's __doc__ and __name__ attributes are filled in;
	the caller is responsible for providing a __file__ attribute."""
		dll.PyModule_GetDict.restype = POINTER(PyObject)
		dll.PyModule_GetDict.argtypes = [ POINTER(PyObject) ]
		dll.PyModule_GetDict.__doc__ = """Return value: Borrowed reference. Return the dictionary object that implements module 's namespace; this object
	is the same as the __dict__ attribute of the module object.  This
	function never fails.  It is recommended extensions use other PyModule_*() and PyObject_*() functions rather than directly
	manipulate a module's __dict__ ."""
		dll.PyModule_GetName.restype = c_char_p
		dll.PyModule_GetName.argtypes = [ POINTER(PyObject) ]
		dll.PyModule_GetName.__doc__ = """Return module 's __name__ value.  If the module does not provide one,
	or if it is not a string, SystemError is raised and NULL is returned."""
		dll.PyModule_GetFilename.restype = c_char_p
		dll.PyModule_GetFilename.argtypes = [ POINTER(PyObject) ]
		dll.PyModule_GetFilename.__doc__ = """Return the name of the file from which module was loaded using module 's __file__ attribute.  If this is not defined, or if it is not a string,
	raise SystemError and return NULL ."""
		dll._PyModule_Clear.restype = None
		dll._PyModule_Clear.argtypes = [ POINTER(PyObject) ]
		dll.PyFunction_New.restype = POINTER(PyObject)
		dll.PyFunction_New.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyFunction_New.__doc__ = """Return value: New reference. Return a new function object associated with the code object code . globals must be a dictionary with the global variables accessible to the function. The function's docstring, name and __module__ are retrieved from the code
	object, the argument defaults and closure are set to NULL ."""
		dll.PyFunction_GetCode.restype = POINTER(PyObject)
		dll.PyFunction_GetCode.argtypes = [ POINTER(PyObject) ]
		dll.PyFunction_GetCode.__doc__ = """Return value: Borrowed reference. Return the code object associated with the function object op ."""
		dll.PyFunction_GetGlobals.restype = POINTER(PyObject)
		dll.PyFunction_GetGlobals.argtypes = [ POINTER(PyObject) ]
		dll.PyFunction_GetGlobals.__doc__ = """Return value: Borrowed reference. Return the globals dictionary associated with the function object op ."""
		dll.PyFunction_GetModule.restype = POINTER(PyObject)
		dll.PyFunction_GetModule.argtypes = [ POINTER(PyObject) ]
		dll.PyFunction_GetModule.__doc__ = """Return value: Borrowed reference. Return the __module__ attribute of the function object op . This is normally
	a string containing the module name, but can be set to any other object by
	Python code."""
		dll.PyFunction_GetDefaults.restype = POINTER(PyObject)
		dll.PyFunction_GetDefaults.argtypes = [ POINTER(PyObject) ]
		dll.PyFunction_GetDefaults.__doc__ = """Return value: Borrowed reference. Return the argument default values of the function object op . This can be a
	tuple of arguments or NULL ."""
		dll.PyFunction_SetDefaults.restype = c_int
		dll.PyFunction_SetDefaults.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyFunction_SetDefaults.__doc__ = """Set the argument default values for the function object op . defaults must be Py_None or a tuple. Raises SystemError and returns -1 on failure."""
		dll.PyFunction_GetClosure.restype = POINTER(PyObject)
		dll.PyFunction_GetClosure.argtypes = [ POINTER(PyObject) ]
		dll.PyFunction_GetClosure.__doc__ = """Return value: Borrowed reference. Return the closure associated with the function object op . This can be NULL or a tuple of cell objects."""
		dll.PyFunction_SetClosure.restype = c_int
		dll.PyFunction_SetClosure.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyFunction_SetClosure.__doc__ = """Set the closure associated with the function object op . closure must be Py_None or a tuple of cell objects. Raises SystemError and returns -1 on failure."""
		dll.PyClassMethod_New.restype = POINTER(PyObject)
		dll.PyClassMethod_New.argtypes = [ POINTER(PyObject) ]
		dll.PyStaticMethod_New.restype = POINTER(PyObject)
		dll.PyStaticMethod_New.argtypes = [ POINTER(PyObject) ]
		dll.PyClass_New.restype = POINTER(PyObject)
		dll.PyClass_New.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyInstance_New.restype = POINTER(PyObject)
		dll.PyInstance_New.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyInstance_New.__doc__ = """Return value: New reference. Create a new instance of a specific class.  The parameters arg and kw are
	used as the positional and keyword parameters to the object's constructor."""
		dll.PyInstance_NewRaw.restype = POINTER(PyObject)
		dll.PyInstance_NewRaw.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyInstance_NewRaw.__doc__ = """Return value: New reference. Create a new instance of a specific class without calling its constructor. class is the class of new object.  The dict parameter will be used as the
	object's __dict__ ; if NULL , a new dictionary will be created for the
	instance."""
		dll.PyMethod_New.restype = POINTER(PyObject)
		dll.PyMethod_New.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyMethod_New.__doc__ = """Return value: New reference. Return a new method object, with func being any callable object; this is the
	function that will be called when the method is called.  If this method should
	be bound to an instance, self should be the instance and class should be the
	class of self , otherwise self should be NULL and class should be the
	class which provides the unbound method.."""
		dll.PyMethod_Function.restype = POINTER(PyObject)
		dll.PyMethod_Function.argtypes = [ POINTER(PyObject) ]
		dll.PyMethod_Function.__doc__ = """Return value: Borrowed reference. Return the function object associated with the method meth ."""
		dll.PyMethod_Self.restype = POINTER(PyObject)
		dll.PyMethod_Self.argtypes = [ POINTER(PyObject) ]
		dll.PyMethod_Self.__doc__ = """Return value: Borrowed reference. Return the instance associated with the method meth if it is bound, otherwise
	return NULL ."""
		dll.PyMethod_Class.restype = POINTER(PyObject)
		dll.PyMethod_Class.argtypes = [ POINTER(PyObject) ]
		dll.PyMethod_Class.__doc__ = """Return value: Borrowed reference. Return the class object from which the method meth was created; if this was
	created from an instance, it will be the class of the instance."""
		dll._PyInstance_Lookup.restype = POINTER(PyObject)
		dll._PyInstance_Lookup.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyClass_IsSubclass.restype = c_int
		dll.PyClass_IsSubclass.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyClass_IsSubclass.__doc__ = """Return true if klass is a subclass of base . Return false in all other cases."""
		dll.PyMethod_ClearFreeList.restype = c_int
		dll.PyMethod_ClearFreeList.argtypes = [  ]
		dll.PyMethod_ClearFreeList.__doc__ = """Clear the free list. Return the total number of freed items. New in version 2.6."""
		dll.PyFile_FromString.restype = POINTER(PyObject)
		dll.PyFile_FromString.argtypes = [ c_char_p, c_char_p ]
		dll.PyFile_FromString.__doc__ = """Return value: New reference. On success, return a new file object that is opened on the file given by filename , with a file mode given by mode , where mode has the same
	semantics as the standard C routine fopen() .  On failure, return NULL ."""
		dll.PyFile_SetBufSize.restype = None
		dll.PyFile_SetBufSize.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyFile_SetBufSize.__doc__ = """Available on systems with setvbuf() only.  This should only be called
	immediately after file object creation."""
		dll.PyFile_SetEncoding.restype = c_int
		dll.PyFile_SetEncoding.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyFile_SetEncoding.__doc__ = """Set the file's encoding for Unicode output to enc . Return 1 on success and 0
	on failure. New in version 2.3."""
		dll.PyFile_SetEncodingAndErrors.restype = c_int
		dll.PyFile_SetEncodingAndErrors.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyFile_SetEncodingAndErrors.__doc__ = """Set the file's encoding for Unicode output to enc , and its error
	mode to err . Return 1 on success and 0 on failure. New in version 2.6."""
		dll.PyFile_AsFile.restype = POINTER(FILE)
		dll.PyFile_AsFile.argtypes = [ POINTER(PyObject) ]
		dll.PyFile_AsFile.__doc__ = """Return the file object associated with p as a FILE* . If the caller will ever use the returned FILE* object while
	the GIL is released it must also call the PyFile_IncUseCount() and PyFile_DecUseCount() functions described below as appropriate."""
		dll.PyFile_IncUseCount.restype = None
		dll.PyFile_IncUseCount.argtypes = [ POINTER(py_object) ]
		dll.PyFile_IncUseCount.__doc__ = """Increments the PyFileObject's internal use count to indicate
	that the underlying FILE* is being used.
	This prevents Python from calling f_close() on it from another thread.
	Callers of this must call PyFile_DecUseCount() when they are
	finished with the FILE* .  Otherwise the file object will
	never be closed by Python. The GIL must be held while calling this function. The suggested use is to call this after PyFile_AsFile() and before
	you release the GIL: FILE * fp = PyFile_AsFile ( p ); PyFile_IncUseCount ( p ); /* ... */ Py_BEGIN_ALLOW_THREADS do_something ( fp ); Py_END_ALLOW_THREADS /* ... */ PyFile_DecUseCount ( p ); New in version 2.6."""
		dll.PyFile_DecUseCount.restype = None
		dll.PyFile_DecUseCount.argtypes = [ POINTER(py_object) ]
		dll.PyFile_DecUseCount.__doc__ = """Decrements the PyFileObject's internal unlocked_count member to
	indicate that the caller is done with its own use of the FILE* .
	This may only be called to undo a prior call to PyFile_IncUseCount() . The GIL must be held while calling this function (see the example
	above). New in version 2.6."""
		dll.PyFile_Name.restype = POINTER(PyObject)
		dll.PyFile_Name.argtypes = [ POINTER(PyObject) ]
		dll.PyFile_Name.__doc__ = """Return value: Borrowed reference. Return the name of the file specified by p as a string object."""
		dll.PyFile_GetLine.restype = POINTER(PyObject)
		dll.PyFile_GetLine.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyFile_GetLine.__doc__ = """Return value: New reference. Equivalent to p.readline([n]) , this function reads one line from the
	object p . p may be a file object or any object with a readline() method.  If n is 0 , exactly one line is read, regardless of the length of
	the line.  If n is greater than 0 , no more than n bytes will be read
	from the file; a partial line can be returned.  In both cases, an empty string
	is returned if the end of the file is reached immediately.  If n is less than 0 , however, one line is read regardless of length, but EOFError is
	raised if the end of the file is reached immediately."""
		dll.PyFile_WriteObject.restype = c_int
		dll.PyFile_WriteObject.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_int ]
		dll.PyFile_WriteObject.__doc__ = """Write object obj to file object p .  The only supported flag for flags is Py_PRINT_RAW ; if given, the str() of the object is written
	instead of the repr() .  Return 0 on success or -1 on failure; the
	appropriate exception will be set."""
		dll.PyFile_SoftSpace.restype = c_int
		dll.PyFile_SoftSpace.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyFile_SoftSpace.__doc__ = """This function exists for internal use by the interpreter.  Set the softspace attribute of p to newflag and return the previous value. p does not have to be a file object for this function to work properly; any
	object is supported (thought its only interesting if the softspace attribute can be set).  This function clears any errors, and will return 0 as the previous value if the attribute either does not exist or if there were
	errors in retrieving it.  There is no way to detect errors from this function,
	but doing so should not be needed."""
		dll.PyFile_WriteString.restype = c_int
		dll.PyFile_WriteString.argtypes = [ c_char_p, POINTER(PyObject) ]
		dll.PyFile_WriteString.__doc__ = """Write string s to file object p .  Return 0 on success or -1 on
	failure; the appropriate exception will be set."""
		dll.PyObject_AsFileDescriptor.restype = c_int
		dll.PyObject_AsFileDescriptor.argtypes = [ POINTER(PyObject) ]
		dll.PyObject_AsFileDescriptor.__doc__ = """Derives a file descriptor from a Python object.  If the object is an integer or
	long integer, its value is returned.  If not, the object's fileno() method
	is called if it exists; the method must return an integer or long integer, which
	is returned as the file descriptor value.  Returns -1 on failure."""
		dll.Py_UniversalNewlineFgets.restype = c_char_p
		dll.Py_UniversalNewlineFgets.argtypes = [ c_char_p, c_int, POINTER(FILE), POINTER(PyObject) ]
		dll.Py_UniversalNewlineFread.restype = c_size_t
		dll.Py_UniversalNewlineFread.argtypes = [ c_char_p, c_size_t, POINTER(FILE), POINTER(PyObject) ]
		dll._PyFile_SanitizeMode.restype = c_int
		dll._PyFile_SanitizeMode.argtypes = [ c_char_p ]
		dll._PyVerify_fd.restype = c_int
		dll._PyVerify_fd.argtypes = [ c_int ]
		dll.PyCObject_FromVoidPtr.restype = POINTER(PyObject)
		dll.PyCObject_FromVoidPtr.argtypes = [ c_void_p, CFUNCTYPE(None, (c_void_p,)) ]
		dll.PyCObject_FromVoidPtr.__doc__ = """Return value: New reference. Create a PyCObject from the void * cobj .  The destr function
	will be called when the object is reclaimed, unless it is NULL ."""
		dll.PyCObject_FromVoidPtrAndDesc.restype = POINTER(PyObject)
		dll.PyCObject_FromVoidPtrAndDesc.argtypes = [ c_void_p, c_void_p, CFUNCTYPE(None, (c_void_p, c_void_p)) ]
		dll.PyCObject_FromVoidPtrAndDesc.__doc__ = """Return value: New reference. Create a PyCObject from the void * cobj .  The destr function will be called when the object is reclaimed. The desc argument can
	be used to pass extra callback data for the destructor function."""
		dll.PyCObject_AsVoidPtr.restype = c_void_p
		dll.PyCObject_AsVoidPtr.argtypes = [ POINTER(PyObject) ]
		dll.PyCObject_AsVoidPtr.__doc__ = """Return the object void * that the PyCObject self was
	created with."""
		dll.PyCObject_GetDesc.restype = c_void_p
		dll.PyCObject_GetDesc.argtypes = [ POINTER(PyObject) ]
		dll.PyCObject_GetDesc.__doc__ = """Return the description void * that the PyCObject self was
	created with."""
		dll.PyCObject_Import.restype = c_void_p
		dll.PyCObject_Import.argtypes = [ c_char_p, c_char_p ]
		dll.PyCObject_SetVoidPtr.restype = c_int
		dll.PyCObject_SetVoidPtr.argtypes = [ POINTER(PyObject), c_void_p ]
		dll.PyCObject_SetVoidPtr.__doc__ = """Set the void pointer inside self to cobj . The PyCObject must not
	have an associated destructor. Return true on success, false on failure."""
		dll.PyCapsule_New.restype = POINTER(PyObject)
		dll.PyCapsule_New.argtypes = [ c_void_p, c_char_p, py_object ]
		dll.PyCapsule_New.__doc__ = """Return value: New reference. Create a PyCapsule encapsulating the pointer .  The pointer argument may not be NULL . On failure, set an exception and return NULL . The name string may either be NULL or a pointer to a valid C string.  If
	non- NULL , this string must outlive the capsule.  (Though it is permitted to
	free it inside the destructor .) If the destructor argument is not NULL , it will be called with the
	capsule as its argument when it is destroyed. If this capsule will be stored as an attribute of a module, the name should
	be specified as modulename.attributename .  This will enable other modules
	to import the capsule using PyCapsule_Import() ."""
		dll.PyCapsule_GetPointer.restype = c_void_p
		dll.PyCapsule_GetPointer.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyCapsule_GetPointer.__doc__ = """Retrieve the pointer stored in the capsule.  On failure, set an exception
	and return NULL . The name parameter must compare exactly to the name stored in the capsule.
	If the name stored in the capsule is NULL , the name passed in must also
	be NULL .  Python uses the C function strcmp() to compare capsule
	names."""
		dll.PyCapsule_GetDestructor.restype = py_object
		dll.PyCapsule_GetDestructor.argtypes = [ POINTER(PyObject) ]
		dll.PyCapsule_GetDestructor.__doc__ = """Return the current destructor stored in the capsule.  On failure, set an
	exception and return NULL . It is legal for a capsule to have a NULL destructor.  This makes a NULL return code somewhat ambiguous; use PyCapsule_IsValid() or PyErr_Occurred() to disambiguate."""
		dll.PyCapsule_GetName.restype = c_char_p
		dll.PyCapsule_GetName.argtypes = [ POINTER(PyObject) ]
		dll.PyCapsule_GetName.__doc__ = """Return the current name stored in the capsule.  On failure, set an exception
	and return NULL . It is legal for a capsule to have a NULL name.  This makes a NULL return
	code somewhat ambiguous; use PyCapsule_IsValid() or PyErr_Occurred() to disambiguate."""
		dll.PyCapsule_GetContext.restype = c_void_p
		dll.PyCapsule_GetContext.argtypes = [ POINTER(PyObject) ]
		dll.PyCapsule_GetContext.__doc__ = """Return the current context stored in the capsule.  On failure, set an
	exception and return NULL . It is legal for a capsule to have a NULL context.  This makes a NULL return code somewhat ambiguous; use PyCapsule_IsValid() or PyErr_Occurred() to disambiguate."""
		dll.PyCapsule_IsValid.restype = c_int
		dll.PyCapsule_IsValid.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyCapsule_IsValid.__doc__ = """Determines whether or not capsule is a valid capsule.  A valid capsule is
	non- NULL , passes PyCapsule_CheckExact() , has a non- NULL pointer
	stored in it, and its internal name matches the name parameter.  (See PyCapsule_GetPointer() for information on how capsule names are
	compared.) In other words, if PyCapsule_IsValid() returns a true value, calls to
	any of the accessors (any function starting with PyCapsule_Get() ) are
	guaranteed to succeed. Return a nonzero value if the object is valid and matches the name passed in.
	Return 0 otherwise.  This function will not fail."""
		dll.PyCapsule_SetPointer.restype = c_int
		dll.PyCapsule_SetPointer.argtypes = [ POINTER(PyObject), c_void_p ]
		dll.PyCapsule_SetPointer.__doc__ = """Set the void pointer inside capsule to pointer .  The pointer may not be NULL . Return 0 on success.  Return nonzero and set an exception on failure."""
		dll.PyCapsule_SetDestructor.restype = c_int
		dll.PyCapsule_SetDestructor.argtypes = [ POINTER(PyObject), py_object ]
		dll.PyCapsule_SetDestructor.__doc__ = """Set the destructor inside capsule to destructor . Return 0 on success.  Return nonzero and set an exception on failure."""
		dll.PyCapsule_SetName.restype = c_int
		dll.PyCapsule_SetName.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyCapsule_SetName.__doc__ = """Set the name inside capsule to name .  If non- NULL , the name must
	outlive the capsule.  If the previous name stored in the capsule was not NULL , no attempt is made to free it. Return 0 on success.  Return nonzero and set an exception on failure."""
		dll.PyCapsule_SetContext.restype = c_int
		dll.PyCapsule_SetContext.argtypes = [ POINTER(PyObject), c_void_p ]
		dll.PyCapsule_SetContext.__doc__ = """Set the context pointer inside capsule to context . Return 0 on success.  Return nonzero and set an exception on failure."""
		dll.PyCapsule_Import.restype = c_void_p
		dll.PyCapsule_Import.argtypes = [ c_char_p, c_int ]
		dll.PyCapsule_Import.__doc__ = """Import a pointer to a C object from a capsule attribute in a module.  The name parameter should specify the full name to the attribute, as in module.attribute .  The name stored in the capsule must match this
	string exactly.  If no_block is true, import the module without blocking
	(using PyImport_ImportModuleNoBlock() ).  If no_block is false,
	import the module conventionally (using PyImport_ImportModule() ). Return the capsule's internal pointer on success.  On failure, set an
	exception and return NULL .  However, if PyCapsule_Import() failed to
	import the module, and no_block was true, no exception is set."""
		dll.PyTraceBack_Here.restype = c_int
		dll.PyTraceBack_Here.argtypes = [ c_void_p ]
		dll.PyTraceBack_Print.restype = c_int
		dll.PyTraceBack_Print.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll._Py_DisplaySourceLine.restype = c_int
		dll._Py_DisplaySourceLine.argtypes = [ POINTER(PyObject), c_char_p, c_int, c_int ]
		dll.PySlice_New.restype = POINTER(PyObject)
		dll.PySlice_New.argtypes = [ POINTER(py_object), POINTER(py_object), POINTER(PyObject) ]
		dll.PySlice_New.__doc__ = """Return value: New reference. Return a new slice object with the given values.  The start , stop , and step parameters are used as the values of the slice object attributes of
	the same names.  Any of the values may be NULL , in which case the None will be used for the corresponding attribute.  Return NULL if
	the new object could not be allocated."""
		dll._PySlice_FromIndices.restype = POINTER(PyObject)
		dll._PySlice_FromIndices.argtypes = [ c_ssize_t, c_ssize_t ]
		dll.PySlice_GetIndices.restype = c_int
		dll.PySlice_GetIndices.argtypes = [ POINTER(py_object), c_ssize_t, POINTER(c_ssize_t), POINTER(c_ssize_t), POINTER(c_ssize_t) ]
		dll.PySlice_GetIndices.__doc__ = """Retrieve the start, stop and step indices from the slice object slice ,
	assuming a sequence of length length . Treats indices greater than length as errors. Returns 0 on success and -1 on error with no exception set (unless one of
	the indices was not None and failed to be converted to an integer,
	in which case -1 is returned with an exception set). You probably do not want to use this function.  If you want to use slice
	objects in versions of Python prior to 2.3, you would probably do well to
	incorporate the source of PySlice_GetIndicesEx() , suitably renamed,
	in the source of your extension. Changed in version 2.5: This function used an c_int type for length and an c_int * type for start , stop , and step . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PySlice_GetIndicesEx.restype = c_int
		dll.PySlice_GetIndicesEx.argtypes = [ POINTER(py_object), c_ssize_t, POINTER(c_ssize_t), POINTER(c_ssize_t), POINTER(c_ssize_t), POINTER(c_ssize_t) ]
		dll.PySlice_GetIndicesEx.__doc__ = """Usable replacement for PySlice_GetIndices() .  Retrieve the start,
	stop, and step indices from the slice object slice assuming a sequence of
	length length , and store the length of the slice in slicelength .  Out
	of bounds indices are clipped in a manner consistent with the handling of
	normal slices. Returns 0 on success and -1 on error with exception set. New in version 2.3. Changed in version 2.5: This function used an c_int type for length and an c_int * type for start , stop , step , and slicelength . This
	might require changes in your code for properly supporting 64-bit
	systems."""
		dll.PyCell_New.restype = POINTER(PyObject)
		dll.PyCell_New.argtypes = [ POINTER(PyObject) ]
		dll.PyCell_New.__doc__ = """Return value: New reference. Create and return a new cell object containing the value ob . The parameter may
	be NULL ."""
		dll.PyCell_Get.restype = POINTER(PyObject)
		dll.PyCell_Get.argtypes = [ POINTER(PyObject) ]
		dll.PyCell_Get.__doc__ = """Return value: New reference. Return the contents of the cell cell ."""
		dll.PyCell_Set.restype = c_int
		dll.PyCell_Set.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyCell_Set.__doc__ = """Set the contents of the cell object cell to value .  This releases the
	reference to any current content of the cell. value may be NULL . cell must be non- NULL ; if it is not a cell object, -1 will be returned.  On
	success, 0 will be returned."""
		dll.PySeqIter_New.restype = POINTER(PyObject)
		dll.PySeqIter_New.argtypes = [ POINTER(PyObject) ]
		dll.PySeqIter_New.__doc__ = """Return value: New reference. Return an iterator that works with a general sequence object, seq .  The
	iteration ends when the sequence raises IndexError for the subscripting
	operation. New in version 2.2."""
		dll.PyCallIter_New.restype = POINTER(PyObject)
		dll.PyCallIter_New.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyCallIter_New.__doc__ = """Return value: New reference. Return a new iterator.  The first parameter, callable , can be any Python
	callable object that can be called with no parameters; each call to it should
	return the next item in the iteration.  When callable returns a value equal to sentinel , the iteration will be terminated. New in version 2.2."""
		dll.PyGen_New.restype = POINTER(PyObject)
		dll.PyGen_New.argtypes = [ POINTER(c_void_p) ]
		dll.PyGen_New.__doc__ = """Return value: New reference. Create and return a new generator object based on the frame object. A
	reference to frame is stolen by this function. The parameter must not be NULL ."""
		dll.PyGen_NeedsFinalizing.restype = c_int
		dll.PyGen_NeedsFinalizing.argtypes = [ POINTER(py_object) ]
		dll.PyDescr_NewMethod.restype = POINTER(PyObject)
		dll.PyDescr_NewMethod.argtypes = [ POINTER(py_object), POINTER(py_object) ]
		dll.PyDescr_NewMethod.__doc__ = """Return value: New reference. New in version 2.2."""
		dll.PyDescr_NewClassMethod.restype = POINTER(PyObject)
		dll.PyDescr_NewClassMethod.argtypes = [ POINTER(py_object), POINTER(py_object) ]
		dll.PyDescr_NewClassMethod.__doc__ = """Return value: New reference. New in version 2.3."""
		dll.PyDescr_NewMember.restype = POINTER(PyObject)
		dll.PyDescr_NewMember.argtypes = [ POINTER(py_object), c_void_p ]
		dll.PyDescr_NewMember.__doc__ = """Return value: New reference. New in version 2.2."""
		dll.PyDescr_NewGetSet.restype = POINTER(PyObject)
		dll.PyDescr_NewGetSet.argtypes = [ POINTER(py_object), LPPyGetSetDef ]
		dll.PyDescr_NewGetSet.__doc__ = """Return value: New reference. New in version 2.2."""
		dll.PyDescr_NewWrapper.restype = POINTER(PyObject)
		# POINTER(struct wrapperbase)
		dll.PyDescr_NewWrapper.argtypes = [ POINTER(py_object), c_void_p, c_void_p ]
		dll.PyDescr_NewWrapper.__doc__ = """Return value: New reference. New in version 2.2."""
		dll.PyDictProxy_New.restype = POINTER(PyObject)
		dll.PyDictProxy_New.argtypes = [ POINTER(PyObject) ]
		dll.PyDictProxy_New.__doc__ = """Return value: New reference. Return a proxy object for a mapping which enforces read-only behavior.
	This is normally used to create a proxy to prevent modification of the
	dictionary for non-dynamic class types. New in version 2.2."""
		dll.PyWrapper_New.restype = POINTER(PyObject)
		dll.PyWrapper_New.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyWrapper_New.__doc__ = """Return value: New reference. New in version 2.2."""
		dll._PyWarnings_Init.restype = None
		dll._PyWarnings_Init.argtypes = [  ]
		dll.PyErr_WarnEx.restype = c_int
		dll.PyErr_WarnEx.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t ]
		dll.PyErr_WarnEx.__doc__ = """Issue a warning message.  The category argument is a warning category (see
	below) or NULL ; the message argument is a message string. stacklevel is a
	positive number giving a number of stack frames; the warning will be issued from
	the  currently executing line of code in that stack frame.  A stacklevel of 1
	is the function calling PyErr_WarnEx() , 2 is  the function above that,
	and so forth. This function normally prints a warning message to sys.stderr ; however, it is
	also possible that the user has specified that warnings are to be turned into
	errors, and in that case this will raise an exception.  It is also possible that
	the function raises an exception because of a problem with the warning machinery
	(the implementation imports the warnings module to do the heavy lifting).
	The return value is 0 if no exception is raised, or -1 if an exception
	is raised.  (It is not possible to determine whether a warning message is
	actually printed, nor what the reason is for the exception; this is
	intentional.)  If an exception is raised, the caller should do its normal
	exception handling (for example, Py_DECREF() owned references and return
	an error value). Warning categories must be subclasses of Warning ; the default warning
	category is RuntimeWarning .  The standard Python warning categories are
	available as global variables whose names are PyExc_ followed by the Python
	exception name. These have the type PyObject* ; they are all class
	objects. Their names are PyExc_Warning , PyExc_UserWarning , PyExc_UnicodeWarning , PyExc_DeprecationWarning , PyExc_SyntaxWarning , PyExc_RuntimeWarning , and PyExc_FutureWarning . PyExc_Warning is a subclass of PyExc_Exception ; the other warning categories are subclasses of PyExc_Warning . For information about warning control, see the documentation for the warnings module and the -W option in the command line
	documentation.  There is no C API for warning control."""
		dll.PyErr_WarnExplicit.restype = c_int
		dll.PyErr_WarnExplicit.argtypes = [ POINTER(PyObject), c_char_p, c_char_p, c_int, c_char_p, POINTER(PyObject) ]
		dll.PyErr_WarnExplicit.__doc__ = """Issue a warning message with explicit control over all warning attributes.  This
	is a straightforward wrapper around the Python function warnings.warn_explicit() , see there for more information.  The module and registry arguments may be set to NULL to get the default effect
	described there."""
		dll.PyWeakref_NewRef.restype = POINTER(PyObject)
		dll.PyWeakref_NewRef.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyWeakref_NewRef.__doc__ = """Return value: New reference. Return a weak reference object for the object ob .  This will always return
	a new reference, but is not guaranteed to create a new object; an existing
	reference object may be returned.  The second parameter, callback , can be a
	callable object that receives notification when ob is garbage collected; it
	should accept a single parameter, which will be the weak reference object
	itself. callback may also be None or NULL .  If ob is not a
	weakly-referencable object, or if callback is not callable, None , or NULL , this will return NULL and raise TypeError . New in version 2.2."""
		dll.PyWeakref_NewProxy.restype = POINTER(PyObject)
		dll.PyWeakref_NewProxy.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyWeakref_NewProxy.__doc__ = """Return value: New reference. Return a weak reference proxy object for the object ob .  This will always
	return a new reference, but is not guaranteed to create a new object; an
	existing proxy object may be returned.  The second parameter, callback , can
	be a callable object that receives notification when ob is garbage
	collected; it should accept a single parameter, which will be the weak
	reference object itself. callback may also be None or NULL .  If ob is not a weakly-referencable object, or if callback is not callable, None , or NULL , this will return NULL and raise TypeError . New in version 2.2."""
		dll.PyWeakref_GetObject.restype = POINTER(PyObject)
		dll.PyWeakref_GetObject.argtypes = [ POINTER(PyObject) ]
		dll.PyWeakref_GetObject.__doc__ = """Return value: Borrowed reference. Return the referenced object from a weak reference, ref .  If the referent is
	no longer live, returns Py_None . New in version 2.2. Warning This function returns a borrowed reference to the referenced object.
	This means that you should always call Py_INCREF() on the object
	except if you know that it cannot be destroyed while you are still
	using it."""
		dll._PyWeakref_GetWeakrefCount.restype = c_ssize_t
		dll._PyWeakref_GetWeakrefCount.argtypes = [ POINTER(py_object) ]
		dll._PyWeakref_ClearRef.restype = None
		dll._PyWeakref_ClearRef.argtypes = [ POINTER(py_object) ]
		dll.PyCodec_Register.restype = c_int
		dll.PyCodec_Register.argtypes = [ POINTER(PyObject) ]
		dll.PyCodec_Register.__doc__ = """Register a new codec search function. As side effect, this tries to load the encodings package, if not yet
	done, to make sure that it is always first in the list of search functions."""
		dll._PyCodec_Lookup.restype = POINTER(PyObject)
		dll._PyCodec_Lookup.argtypes = [ c_char_p ]
		dll.PyCodec_Encode.restype = POINTER(PyObject)
		dll.PyCodec_Encode.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyCodec_Encode.__doc__ = """Generic codec based encoding API. object is passed through the encoder function found for the given encoding using the error handling method defined by errors . errors may
	be NULL to use the default method defined for the codec.  Raises a LookupError if no encoder can be found."""
		dll.PyCodec_Decode.restype = POINTER(PyObject)
		dll.PyCodec_Decode.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyCodec_Decode.__doc__ = """Generic codec based decoding API. object is passed through the decoder function found for the given encoding using the error handling method defined by errors . errors may
	be NULL to use the default method defined for the codec.  Raises a LookupError if no encoder can be found."""
		dll.PyCodec_Encoder.restype = POINTER(PyObject)
		dll.PyCodec_Encoder.argtypes = [ c_char_p ]
		dll.PyCodec_Encoder.__doc__ = """Get an encoder function for the given encoding ."""
		dll.PyCodec_Decoder.restype = POINTER(PyObject)
		dll.PyCodec_Decoder.argtypes = [ c_char_p ]
		dll.PyCodec_Decoder.__doc__ = """Get a decoder function for the given encoding ."""
		dll.PyCodec_IncrementalEncoder.restype = POINTER(PyObject)
		dll.PyCodec_IncrementalEncoder.argtypes = [ c_char_p, c_char_p ]
		dll.PyCodec_IncrementalEncoder.__doc__ = """Get an IncrementalEncoder object for the given encoding ."""
		dll.PyCodec_IncrementalDecoder.restype = POINTER(PyObject)
		dll.PyCodec_IncrementalDecoder.argtypes = [ c_char_p, c_char_p ]
		dll.PyCodec_IncrementalDecoder.__doc__ = """Get an IncrementalDecoder object for the given encoding ."""
		dll.PyCodec_StreamReader.restype = POINTER(PyObject)
		dll.PyCodec_StreamReader.argtypes = [ c_char_p, POINTER(PyObject), c_char_p ]
		dll.PyCodec_StreamReader.__doc__ = """Get a StreamReader factory function for the given encoding ."""
		dll.PyCodec_StreamWriter.restype = POINTER(PyObject)
		dll.PyCodec_StreamWriter.argtypes = [ c_char_p, POINTER(PyObject), c_char_p ]
		dll.PyCodec_StreamWriter.__doc__ = """Get a StreamWriter factory function for the given encoding ."""
		dll.PyCodec_RegisterError.restype = c_int
		dll.PyCodec_RegisterError.argtypes = [ c_char_p, POINTER(PyObject) ]
		dll.PyCodec_RegisterError.__doc__ = """Register the error handling callback function error under the given name .
	This callback function will be called by a codec when it encounters
	unencodable characters/undecodable bytes and name is specified as the error
	parameter in the call to the encode/decode function. The callback gets a single argument, an instance of UnicodeEncodeError , UnicodeDecodeError or UnicodeTranslateError that holds information about the problematic
	sequence of characters or bytes and their offset in the original string (see Unicode Exception Objects for functions to extract this information).  The
	callback must either raise the given exception, or return a two-item tuple
	containing the replacement for the problematic sequence, and an integer
	giving the offset in the original string at which encoding/decoding should be
	resumed. Return 0 on success, -1 on error."""
		dll.PyCodec_LookupError.restype = POINTER(PyObject)
		dll.PyCodec_LookupError.argtypes = [ c_char_p ]
		dll.PyCodec_LookupError.__doc__ = """Lookup the error handling callback function registered under name .  As a
	special case NULL can be passed, in which case the error handling callback
	for "strict" will be returned."""
		dll.PyCodec_StrictErrors.restype = POINTER(PyObject)
		dll.PyCodec_StrictErrors.argtypes = [ POINTER(PyObject) ]
		dll.PyCodec_StrictErrors.__doc__ = """Raise exc as an exception."""
		dll.PyCodec_IgnoreErrors.restype = POINTER(PyObject)
		dll.PyCodec_IgnoreErrors.argtypes = [ POINTER(PyObject) ]
		dll.PyCodec_IgnoreErrors.__doc__ = """Ignore the unicode error, skipping the faulty input."""
		dll.PyCodec_ReplaceErrors.restype = POINTER(PyObject)
		dll.PyCodec_ReplaceErrors.argtypes = [ POINTER(PyObject) ]
		dll.PyCodec_ReplaceErrors.__doc__ = """Replace the unicode encode error with \\x92 or U+FFFD ."""
		dll.PyCodec_XMLCharRefReplaceErrors.restype = POINTER(PyObject)
		dll.PyCodec_XMLCharRefReplaceErrors.argtypes = [ POINTER(PyObject) ]
		dll.PyCodec_XMLCharRefReplaceErrors.__doc__ = """Replace the unicode encode error with XML character references."""
		dll.PyCodec_BackslashReplaceErrors.restype = POINTER(PyObject)
		dll.PyCodec_BackslashReplaceErrors.argtypes = [ POINTER(PyObject) ]
		dll.PyCodec_BackslashReplaceErrors.__doc__ = """Replace the unicode encode error with backslash escapes ( \\x , \\u and \\U )."""
		dll.PyErr_SetNone.restype = None
		dll.PyErr_SetNone.argtypes = [ POINTER(PyObject) ]
		dll.PyErr_SetNone.__doc__ = """This is a shorthand for PyErr_SetObject(type, Py_None) ."""
		dll.PyErr_SetObject.restype = None
		dll.PyErr_SetObject.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyErr_SetObject.__doc__ = """This function is similar to PyErr_SetString() but lets you specify an
	arbitrary Python object for the "value" of the exception."""
		dll.PyErr_SetString.restype = None
		dll.PyErr_SetString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyErr_SetString.__doc__ = """This is the most common way to set the error indicator.  The first argument
	specifies the exception type; it is normally one of the standard exceptions,
	e.g. PyExc_RuntimeError .  You need not increment its reference count.
	The second argument is an error message; it is converted to a string object."""
		dll.PyErr_Occurred.restype = POINTER(PyObject)
		dll.PyErr_Occurred.argtypes = [  ]
		dll.PyErr_Occurred.__doc__ = """Return value: Borrowed reference. Test whether the error indicator is set.  If set, return the exception type (the first argument to the last call to one of the PyErr_Set*() functions or to PyErr_Restore() ).  If not set, return NULL .  You do not
	own a reference to the return value, so you do not need to Py_DECREF() it. Note Do not compare the return value to a specific exception; use PyErr_ExceptionMatches() instead, shown below.  (The comparison could
	easily fail since the exception may be an instance instead of a class, in the
	case of a class exception, or it may the a subclass of the expected exception.)"""
		dll.PyErr_Clear.restype = None
		dll.PyErr_Clear.argtypes = [  ]
		dll.PyErr_Clear.__doc__ = """Clear the error indicator.  If the error indicator is not set, there is no
	effect."""
		dll.PyErr_Fetch.restype = None
		dll.PyErr_Fetch.argtypes = [ POINTER(POINTER(PyObject)), POINTER(POINTER(PyObject)), POINTER(POINTER(PyObject)) ]
		dll.PyErr_Fetch.__doc__ = """Retrieve the error indicator into three variables whose addresses are passed.
	If the error indicator is not set, set all three variables to NULL .  If it is
	set, it will be cleared and you own a reference to each object retrieved.  The
	value and traceback object may be NULL even when the type object is not. Note This function is normally only used by code that needs to handle exceptions or
	by code that needs to save and restore the error indicator temporarily."""
		dll.PyErr_Restore.restype = None
		dll.PyErr_Restore.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyErr_Restore.__doc__ = """Set  the error indicator from the three objects.  If the error indicator is
	already set, it is cleared first.  If the objects are NULL , the error
	indicator is cleared.  Do not pass a NULL type and non- NULL value or
	traceback.  The exception type should be a class.  Do not pass an invalid
	exception type or value. (Violating these rules will cause subtle problems
	later.)  This call takes away a reference to each object: you must own a
	reference to each object before the call and after the call you no longer own
	these references.  (If you don't understand this, don't use this function.  I
	warned you.) Note This function is normally only used by code that needs to save and restore the
	error indicator temporarily; use PyErr_Fetch() to save the current
	exception state."""
		dll.PyErr_GivenExceptionMatches.restype = c_int
		dll.PyErr_GivenExceptionMatches.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyErr_GivenExceptionMatches.__doc__ = """Return true if the given exception matches the exception in exc .  If exc is a class object, this also returns true when given is an instance
	of a subclass.  If exc is a tuple, all exceptions in the tuple (and
	recursively in subtuples) are searched for a match."""
		dll.PyErr_ExceptionMatches.restype = c_int
		dll.PyErr_ExceptionMatches.argtypes = [ POINTER(PyObject) ]
		dll.PyErr_ExceptionMatches.__doc__ = """Equivalent to PyErr_GivenExceptionMatches(PyErr_Occurred(), exc) .  This
	should only be called when an exception is actually set; a memory access
	violation will occur if no exception has been raised."""
		dll.PyErr_NormalizeException.restype = None
		dll.PyErr_NormalizeException.argtypes = [ POINTER(POINTER(PyObject)), POINTER(POINTER(PyObject)), POINTER(POINTER(PyObject)) ]
		dll.PyErr_NormalizeException.__doc__ = """Under certain circumstances, the values returned by PyErr_Fetch() below
	can be "unnormalized", meaning that *exc is a class object but *val is
	not an instance of the  same class.  This function can be used to instantiate
	the class in that case.  If the values are already normalized, nothing happens.
	The delayed normalization is implemented to improve performance."""
		dll.PyErr_BadArgument.restype = c_int
		dll.PyErr_BadArgument.argtypes = [  ]
		dll.PyErr_BadArgument.__doc__ = """This is a shorthand for PyErr_SetString(PyExc_TypeError, message) , where message indicates that a built-in operation was invoked with an illegal
	argument.  It is mostly for internal use."""
		dll.PyErr_NoMemory.restype = POINTER(PyObject)
		dll.PyErr_NoMemory.argtypes = [  ]
		dll.PyErr_NoMemory.__doc__ = """Return value: Always NULL. This is a shorthand for PyErr_SetNone(PyExc_MemoryError) ; it returns NULL so an object allocation function can write return PyErr_NoMemory(); when it
	runs out of memory."""
		dll.PyErr_SetFromErrno.restype = POINTER(PyObject)
		dll.PyErr_SetFromErrno.argtypes = [ POINTER(PyObject) ]
		dll.PyErr_SetFromErrno.__doc__ = """Return value: Always NULL. This is a convenience function to raise an exception when a C library function
	has returned an error and set the C variable errno .  It constructs a
	tuple object whose first item is the integer errno value and whose
	second item is the corresponding error message (gotten from strerror() ),
	and then calls PyErr_SetObject(type, object) .  On Unix, when the errno value is EINTR , indicating an interrupted system call,
	this calls PyErr_CheckSignals() , and if that set the error indicator,
	leaves it set to that.  The function always returns NULL , so a wrapper
	function around a system call can write return PyErr_SetFromErrno(type); when the system call returns an error."""
		dll.PyErr_SetFromErrnoWithFilenameObject.restype = POINTER(PyObject)
		dll.PyErr_SetFromErrnoWithFilenameObject.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyErr_SetFromErrnoWithFilename.restype = POINTER(PyObject)
		dll.PyErr_SetFromErrnoWithFilename.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyErr_SetFromErrnoWithFilename.__doc__ = """Return value: Always NULL. Similar to PyErr_SetFromErrno() , with the additional behavior that if filename is not NULL , it is passed to the constructor of type as a third
	parameter.  In the case of exceptions such as IOError and OSError ,
	this is used to define the filename attribute of the exception instance."""
		dll.PyErr_SetFromErrnoWithUnicodeFilename.restype = POINTER(PyObject)
		dll.PyErr_SetFromErrnoWithUnicodeFilename.argtypes = [ POINTER(PyObject), c_wchar_p ]
		dll.PyErr_SetFromWindowsErrWithFilenameObject.restype = POINTER(PyObject)
		dll.PyErr_SetFromWindowsErrWithFilenameObject.argtypes = [ c_int, c_char_p ]
		dll.PyErr_SetFromWindowsErrWithFilename.restype = POINTER(PyObject)
		dll.PyErr_SetFromWindowsErrWithFilename.argtypes = [ c_int, c_char_p ]
		dll.PyErr_SetFromWindowsErrWithFilename.__doc__ = """Return value: Always NULL. Similar to PyErr_SetFromWindowsErr() , with the additional behavior that
	if filename is not NULL , it is passed to the constructor of WindowsError as a third parameter. Availability: Windows."""
		dll.PyErr_SetFromWindowsErrWithUnicodeFilename.restype = POINTER(PyObject)
		dll.PyErr_SetFromWindowsErrWithUnicodeFilename.argtypes = [ c_int, c_wchar_p ]
		dll.PyErr_SetFromWindowsErr.restype = POINTER(PyObject)
		dll.PyErr_SetFromWindowsErr.argtypes = [ c_int ]
		dll.PyErr_SetFromWindowsErr.__doc__ = """Return value: Always NULL. This is a convenience function to raise WindowsError . If called with ierr of 0 , the error code returned by a call to GetLastError() is used instead.  It calls the Win32 function FormatMessage() to retrieve
	the Windows description of error code given by ierr or GetLastError() ,
	then it constructs a tuple object whose first item is the ierr value and whose
	second item is the corresponding error message (gotten from FormatMessage() ), and then calls PyErr_SetObject(PyExc_WindowsError, object) . This function always returns NULL . Availability: Windows."""
		dll.PyErr_SetExcFromWindowsErrWithFilenameObject.restype = POINTER(PyObject)
		dll.PyErr_SetExcFromWindowsErrWithFilenameObject.argtypes = [ POINTER(PyObject), c_int, POINTER(PyObject) ]
		dll.PyErr_SetExcFromWindowsErrWithFilename.restype = POINTER(PyObject)
		dll.PyErr_SetExcFromWindowsErrWithFilename.argtypes = [ POINTER(PyObject), c_int, c_char_p ]
		dll.PyErr_SetExcFromWindowsErrWithFilename.__doc__ = """Return value: Always NULL. Similar to PyErr_SetFromWindowsErrWithFilename() , with an additional
	parameter specifying the exception type to be raised. Availability: Windows. New in version 2.3."""
		dll.PyErr_SetExcFromWindowsErrWithUnicodeFilename.restype = POINTER(PyObject)
		dll.PyErr_SetExcFromWindowsErrWithUnicodeFilename.argtypes = [ POINTER(PyObject), c_int, c_wchar_p ]
		dll.PyErr_SetExcFromWindowsErr.restype = POINTER(PyObject)
		dll.PyErr_SetExcFromWindowsErr.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyErr_SetExcFromWindowsErr.__doc__ = """Return value: Always NULL. Similar to PyErr_SetFromWindowsErr() , with an additional parameter
	specifying the exception type to be raised. Availability: Windows. New in version 2.3."""
		dll._PyErr_BadInternalCall.restype = None
		dll._PyErr_BadInternalCall.argtypes = [ c_char_p, c_int ]
		dll.PyErr_NewException.restype = POINTER(PyObject)
		dll.PyErr_NewException.argtypes = [ c_char_p, POINTER(PyObject), POINTER(PyObject) ]
		dll.PyErr_NewException.__doc__ = """Return value: New reference. This utility function creates and returns a new exception class. The name argument must be the name of the new exception, a C string of the form module.classname .  The base and dict arguments are normally NULL .
	This creates a class object derived from Exception (accessible in C as PyExc_Exception ). The __module__ attribute of the new class is set to the first part (up
	to the last dot) of the name argument, and the class name is set to the last
	part (after the last dot).  The base argument can be used to specify alternate
	base classes; it can either be only one class or a tuple of classes. The dict argument can be used to specify a dictionary of class variables and methods."""
		dll.PyErr_NewExceptionWithDoc.restype = POINTER(PyObject)
		dll.PyErr_NewExceptionWithDoc.argtypes = [ c_char_p, c_char_p, POINTER(PyObject), POINTER(PyObject) ]
		dll.PyErr_NewExceptionWithDoc.__doc__ = """Return value: New reference. Same as PyErr_NewException() , except that the new exception class can
	easily be given a docstring: If doc is non- NULL , it will be used as the
	docstring for the exception class. New in version 2.7."""
		dll.PyErr_WriteUnraisable.restype = None
		dll.PyErr_WriteUnraisable.argtypes = [ POINTER(PyObject) ]
		dll.PyErr_WriteUnraisable.__doc__ = """This utility function prints a warning message to sys.stderr when an
	exception has been set but it is impossible for the interpreter to actually
	raise the exception.  It is used, for example, when an exception occurs in an __del__() method. The function is called with a single argument obj that identifies the context
	in which the unraisable exception occurred. The repr of obj will be printed in
	the warning message."""
		dll.PyErr_CheckSignals.restype = c_int
		dll.PyErr_CheckSignals.argtypes = [  ]
		dll.PyErr_CheckSignals.__doc__ = """This function interacts with Python's signal handling.  It checks whether a
	signal has been sent to the processes and if so, invokes the corresponding
	signal handler.  If the signal module is supported, this can invoke a
	signal handler written in Python.  In all cases, the default effect for SIGINT is to raise the KeyboardInterrupt exception.  If an
	exception is raised the error indicator is set and the function returns -1 ;
	otherwise the function returns 0 .  The error indicator may or may not be
	cleared if it was previously set."""
		dll.PyErr_SetInterrupt.restype = None
		dll.PyErr_SetInterrupt.argtypes = [  ]
		dll.PyErr_SetInterrupt.__doc__ = """This function simulates the effect of a SIGINT signal arriving - the
	next time PyErr_CheckSignals() is called, KeyboardInterrupt will
	be raised.  It may be called without holding the interpreter lock."""
		dll.PySignal_SetWakeupFd.restype = c_int
		dll.PySignal_SetWakeupFd.argtypes = [ c_int ]
		dll.PySignal_SetWakeupFd.__doc__ = """This utility function specifies a file descriptor to which a '\\0' byte will
	be written whenever a signal is received.  It returns the previous such file
	descriptor.  The value -1 disables the feature; this is the initial state.
	This is equivalent to signal.set_wakeup_fd() in Python, but without any
	error checking. fd should be a valid file descriptor.  The function should
	only be called from the main thread. New in version 2.6."""
		dll.PyErr_SyntaxLocation.restype = None
		dll.PyErr_SyntaxLocation.argtypes = [ c_char_p, c_int ]
		dll.PyErr_ProgramText.restype = POINTER(PyObject)
		dll.PyErr_ProgramText.argtypes = [ c_char_p, c_int ]
		dll.PyUnicodeDecodeError_Create.restype = POINTER(PyObject)
		dll.PyUnicodeDecodeError_Create.argtypes = [ c_char_p, c_char_p, c_ssize_t, c_ssize_t, c_ssize_t, c_char_p ]
		dll.PyUnicodeDecodeError_Create.__doc__ = """Create a UnicodeDecodeError object with the attributes encoding , object , length , start , end and reason ."""
		dll.PyUnicodeEncodeError_Create.restype = POINTER(PyObject)
		dll.PyUnicodeEncodeError_Create.argtypes = [ c_char_p, c_wchar_p, c_ssize_t, c_ssize_t, c_ssize_t, c_char_p ]
		dll.PyUnicodeEncodeError_Create.__doc__ = """Create a UnicodeEncodeError object with the attributes encoding , object , length , start , end and reason ."""
		dll.PyUnicodeTranslateError_Create.restype = POINTER(PyObject)
		dll.PyUnicodeTranslateError_Create.argtypes = [ c_wchar_p, c_ssize_t, c_ssize_t, c_ssize_t, c_char_p ]
		dll.PyUnicodeTranslateError_Create.__doc__ = """Create a UnicodeTranslateError object with the attributes object , length , start , end and reason ."""
		dll.PyUnicodeEncodeError_GetEncoding.restype = POINTER(PyObject)
		dll.PyUnicodeEncodeError_GetEncoding.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeEncodeError_GetEncoding.__doc__ = """Return the encoding attribute of the given exception object."""
		dll.PyUnicodeDecodeError_GetEncoding.restype = POINTER(PyObject)
		dll.PyUnicodeDecodeError_GetEncoding.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeEncodeError_GetObject.restype = POINTER(PyObject)
		dll.PyUnicodeEncodeError_GetObject.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeDecodeError_GetObject.restype = POINTER(PyObject)
		dll.PyUnicodeDecodeError_GetObject.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeTranslateError_GetObject.restype = POINTER(PyObject)
		dll.PyUnicodeTranslateError_GetObject.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeTranslateError_GetObject.__doc__ = """Return the object attribute of the given exception object."""
		dll.PyUnicodeEncodeError_GetStart.restype = c_int
		dll.PyUnicodeEncodeError_GetStart.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PyUnicodeDecodeError_GetStart.restype = c_int
		dll.PyUnicodeDecodeError_GetStart.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PyUnicodeTranslateError_GetStart.restype = c_int
		dll.PyUnicodeTranslateError_GetStart.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PyUnicodeTranslateError_GetStart.__doc__ = """Get the start attribute of the given exception object and place it into *start . start must not be NULL .  Return 0 on success, -1 on
	failure."""
		dll.PyUnicodeEncodeError_SetStart.restype = c_int
		dll.PyUnicodeEncodeError_SetStart.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeDecodeError_SetStart.restype = c_int
		dll.PyUnicodeDecodeError_SetStart.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeTranslateError_SetStart.restype = c_int
		dll.PyUnicodeTranslateError_SetStart.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeTranslateError_SetStart.__doc__ = """Set the start attribute of the given exception object to start .  Return 0 on success, -1 on failure."""
		dll.PyUnicodeEncodeError_GetEnd.restype = c_int
		dll.PyUnicodeEncodeError_GetEnd.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PyUnicodeDecodeError_GetEnd.restype = c_int
		dll.PyUnicodeDecodeError_GetEnd.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PyUnicodeTranslateError_GetEnd.restype = c_int
		dll.PyUnicodeTranslateError_GetEnd.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PyUnicodeTranslateError_GetEnd.__doc__ = """Get the end attribute of the given exception object and place it into *end . end must not be NULL .  Return 0 on success, -1 on
	failure."""
		dll.PyUnicodeEncodeError_SetEnd.restype = c_int
		dll.PyUnicodeEncodeError_SetEnd.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeDecodeError_SetEnd.restype = c_int
		dll.PyUnicodeDecodeError_SetEnd.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeTranslateError_SetEnd.restype = c_int
		dll.PyUnicodeTranslateError_SetEnd.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyUnicodeTranslateError_SetEnd.__doc__ = """Set the end attribute of the given exception object to end .  Return 0 on success, -1 on failure."""
		dll.PyUnicodeEncodeError_GetReason.restype = POINTER(PyObject)
		dll.PyUnicodeEncodeError_GetReason.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeDecodeError_GetReason.restype = POINTER(PyObject)
		dll.PyUnicodeDecodeError_GetReason.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeTranslateError_GetReason.restype = POINTER(PyObject)
		dll.PyUnicodeTranslateError_GetReason.argtypes = [ POINTER(PyObject) ]
		dll.PyUnicodeTranslateError_GetReason.__doc__ = """Return the reason attribute of the given exception object."""
		dll.PyUnicodeEncodeError_SetReason.restype = c_int
		dll.PyUnicodeEncodeError_SetReason.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyUnicodeDecodeError_SetReason.restype = c_int
		dll.PyUnicodeDecodeError_SetReason.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyUnicodeTranslateError_SetReason.restype = c_int
		dll.PyUnicodeTranslateError_SetReason.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyUnicodeTranslateError_SetReason.__doc__ = """Set the reason attribute of the given exception object to reason .  Return 0 on success, -1 on failure."""
		dll.PyInterpreterState_New.restype = POINTER(py_object)
		dll.PyInterpreterState_New.argtypes = [  ]
		dll.PyInterpreterState_New.__doc__ = """Create a new interpreter state object.  The global interpreter lock need not
	be held, but may be held if it is necessary to serialize calls to this
	function."""
		dll.PyInterpreterState_Clear.restype = None
		dll.PyInterpreterState_Clear.argtypes = [ POINTER(py_object) ]
		dll.PyInterpreterState_Clear.__doc__ = """Reset all information in an interpreter state object.  The global interpreter
	lock must be held."""
		dll.PyInterpreterState_Delete.restype = None
		dll.PyInterpreterState_Delete.argtypes = [ POINTER(py_object) ]
		dll.PyInterpreterState_Delete.__doc__ = """Destroy an interpreter state object.  The global interpreter lock need not be
	held.  The interpreter state must have been reset with a previous call to PyInterpreterState_Clear() ."""
		dll.PyThreadState_New.restype = POINTER(py_object)
		dll.PyThreadState_New.argtypes = [ POINTER(py_object) ]
		dll.PyThreadState_New.__doc__ = """Create a new thread state object belonging to the given interpreter object.
	The global interpreter lock need not be held, but may be held if it is
	necessary to serialize calls to this function."""
		dll._PyThreadState_Prealloc.restype = POINTER(py_object)
		dll._PyThreadState_Prealloc.argtypes = [ POINTER(py_object) ]
		dll._PyThreadState_Init.restype = None
		dll._PyThreadState_Init.argtypes = [ POINTER(py_object) ]
		dll.PyThreadState_Clear.restype = None
		dll.PyThreadState_Clear.argtypes = [ POINTER(py_object) ]
		dll.PyThreadState_Clear.__doc__ = """Reset all information in a thread state object.  The global interpreter lock
	must be held."""
		dll.PyThreadState_Delete.restype = None
		dll.PyThreadState_Delete.argtypes = [ POINTER(py_object) ]
		dll.PyThreadState_Delete.__doc__ = """Destroy a thread state object.  The global interpreter lock need not be held.
	The thread state must have been reset with a previous call to PyThreadState_Clear() ."""
		dll.PyThreadState_DeleteCurrent.restype = None
		dll.PyThreadState_DeleteCurrent.argtypes = [  ]
		dll._PyGILState_Reinit.restype = None
		dll._PyGILState_Reinit.argtypes = [  ]
		dll.PyThreadState_Get.restype = POINTER(py_object)
		dll.PyThreadState_Get.argtypes = [  ]
		dll.PyThreadState_Get.__doc__ = """Return the current thread state.  The global interpreter lock must be held.
	When the current thread state is NULL , this issues a fatal error (so that
	the caller needn't check for NULL )."""
		dll.PyThreadState_Swap.restype = POINTER(py_object)
		dll.PyThreadState_Swap.argtypes = [ POINTER(py_object) ]
		dll.PyThreadState_Swap.__doc__ = """Swap the current thread state with the thread state given by the argument tstate , which may be NULL .  The global interpreter lock must be held
	and is not released."""
		dll.PyThreadState_GetDict.restype = POINTER(PyObject)
		dll.PyThreadState_GetDict.argtypes = [  ]
		dll.PyThreadState_GetDict.__doc__ = """Return value: Borrowed reference. Return a dictionary in which extensions can store thread-specific state
	information.  Each extension should use a unique key to use to store state in
	the dictionary.  It is okay to call this function when no current thread state
	is available. If this function returns NULL , no exception has been raised and
	the caller should assume no current thread state is available. Changed in version 2.3: Previously this could only be called when a current thread is active, and NULL meant that an exception was raised."""
		dll.PyThreadState_SetAsyncExc.restype = c_int
		dll.PyThreadState_SetAsyncExc.argtypes = [ c_long, POINTER(PyObject) ]
		dll.PyThreadState_SetAsyncExc.__doc__ = """Asynchronously raise an exception in a thread. The id argument is the thread
	id of the target thread; exc is the exception object to be raised. This
	function does not steal any references to exc . To prevent naive misuse, you
	must write your own C extension to call this.  Must be called with the GIL held.
	Returns the number of thread states modified; this is normally one, but will be
	zero if the thread id isn't found.  If exc is NULL , the pending
	exception (if any) for the thread is cleared. This raises no exceptions. New in version 2.3."""
		dll.PyGILState_Ensure.restype = py_object
		dll.PyGILState_Ensure.argtypes = [  ]
		dll.PyGILState_Ensure.__doc__ = """Ensure that the current thread is ready to call the Python C API regardless
	of the current state of Python, or of the global interpreter lock. This may
	be called as many times as desired by a thread as long as each call is
	matched with a call to PyGILState_Release() . In general, other
	thread-related APIs may be used between PyGILState_Ensure() and PyGILState_Release() calls as long as the thread state is restored to
	its previous state before the Release().  For example, normal usage of the Py_BEGIN_ALLOW_THREADS and Py_END_ALLOW_THREADS macros is
	acceptable. The return value is an opaque "handle" to the thread state when PyGILState_Ensure() was called, and must be passed to PyGILState_Release() to ensure Python is left in the same state. Even
	though recursive calls are allowed, these handles cannot be shared - each
	unique call to PyGILState_Ensure() must save the handle for its call
	to PyGILState_Release() . When the function returns, the current thread will hold the GIL and be able
	to call arbitrary Python code.  Failure is a fatal error. New in version 2.3."""
		dll.PyGILState_Release.restype = None
		dll.PyGILState_Release.argtypes = [ py_object ]
		dll.PyGILState_Release.__doc__ = """Release any resources previously acquired.  After this call, Python's state will
	be the same as it was prior to the corresponding PyGILState_Ensure() call
	(but generally this state will be unknown to the caller, hence the use of the
	GILState API). Every call to PyGILState_Ensure() must be matched by a call to PyGILState_Release() on the same thread. New in version 2.3."""
		dll.PyGILState_GetThisThreadState.restype = POINTER(py_object)
		dll.PyGILState_GetThisThreadState.argtypes = [  ]
		dll.PyGILState_GetThisThreadState.__doc__ = """Get the current thread state for this thread.  May return NULL if no
	GILState API has been used on the current thread.  Note that the main thread
	always has such a thread-state, even if no auto-thread-state call has been
	made on the main thread.  This is mainly a helper/diagnostic function. New in version 2.3."""
		dll._PyThread_CurrentFrames.restype = POINTER(PyObject)
		dll._PyThread_CurrentFrames.argtypes = [  ]
		dll.PyInterpreterState_Head.restype = POINTER(py_object)
		dll.PyInterpreterState_Head.argtypes = [  ]
		dll.PyInterpreterState_Head.__doc__ = """Return the interpreter state object at the head of the list of all such objects. New in version 2.2."""
		dll.PyInterpreterState_Next.restype = POINTER(py_object)
		dll.PyInterpreterState_Next.argtypes = [ POINTER(py_object) ]
		dll.PyInterpreterState_Next.__doc__ = """Return the next interpreter state object after interp from the list of all
	such objects. New in version 2.2."""
		dll.PyInterpreterState_ThreadHead.restype = POINTER(py_object)
		dll.PyInterpreterState_ThreadHead.argtypes = [ POINTER(py_object) ]
		dll.PyInterpreterState_ThreadHead.__doc__ = """Return the a pointer to the first PyThreadState object in the list of
	threads associated with the interpreter interp . New in version 2.2."""
		dll.PyThreadState_Next.restype = POINTER(py_object)
		dll.PyThreadState_Next.argtypes = [ POINTER(py_object) ]
		dll.PyThreadState_Next.__doc__ = """Return the next thread state object after tstate from the list of all such
	objects belonging to the same PyInterpreterState object. New in version 2.2."""
		dll.PyArena_New.restype = POINTER(py_object)
		dll.PyArena_New.argtypes = [  ]
		dll.PyArena_Free.restype = None
		dll.PyArena_Free.argtypes = [ POINTER(py_object) ]
		dll.PyArena_Malloc.restype = c_void_p
		dll.PyArena_Malloc.argtypes = [ POINTER(py_object), c_size_t ]
		dll.PyArena_AddPyObject.restype = c_int
		dll.PyArena_AddPyObject.argtypes = [ POINTER(py_object), POINTER(PyObject) ]
		dll._Py_VaBuildValue_SizeT.restype = POINTER(PyObject)
		dll._Py_VaBuildValue_SizeT.argtypes = [ c_char_p, va_list ]
		dll.PyArg_Parse.restype = c_int
		dll.PyArg_Parse.argtypes = [ POINTER(PyObject), c_char_p, va_list ]
		dll.PyArg_Parse.__doc__ = """Function used to deconstruct the argument lists of "old-style" functions
	- these are functions which use the METH_OLDARGS parameter
	parsing method.  This is not recommended for use in parameter parsing in
	new code, and most code in the standard interpreter has been modified to no
	longer use this for that purpose.  It does remain a convenient way to
	decompose other tuples, however, and may continue to be used for that
	purpose."""
		dll.PyArg_ParseTupleAndKeywords.restype = c_int
		dll.PyArg_ParseTupleAndKeywords.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_char_p, POINTER(c_char_p), va_list ]
		dll.PyArg_ParseTupleAndKeywords.__doc__ = """Parse the parameters of a function that takes both positional and keyword
	parameters into local variables.  Returns true on success; on failure, it
	returns false and raises the appropriate exception."""
		dll.PyArg_UnpackTuple.restype = c_int
		dll.PyArg_UnpackTuple.argtypes = [ POINTER(PyObject), c_char_p, c_ssize_t, c_ssize_t, va_list ]
		dll.PyArg_UnpackTuple.__doc__ = """A simpler form of parameter retrieval which does not use a format string to
	specify the types of the arguments.  Functions which use this method to
	retrieve their parameters should be declared as METH_VARARGS in
	function or method tables.  The tuple containing the actual parameters
	should be passed as args ; it must actually be a tuple.  The length of the
	tuple must be at least min and no more than max ; min and max may be
	equal.  Additional arguments must be passed to the function, each of which
	should be a pointer to a PyObject* variable; these will be filled
	in with the values from args ; they will contain borrowed references.  The
	variables which correspond to optional parameters not given by args will
	not be filled in; these should be initialized by the caller. This function
	returns true on success and false if args is not a tuple or contains the
	wrong number of elements; an exception will be set if there was a failure. This is an example of the use of this function, taken from the sources for
	the _weakref helper module for weak references: static PyObject * weakref_ref ( PyObject * self , PyObject * args ) { PyObject * object ; PyObject * callback = NULL ; PyObject * result = NULL ; if ( PyArg_UnpackTuple ( args , "ref" , 1 , 2 , & object , & callback )) { result = PyWeakref_NewRef ( object , callback ); } return result ; } The call to PyArg_UnpackTuple() in this example is entirely
	equivalent to this call to PyArg_ParseTuple() : PyArg_ParseTuple ( args , "O|O:ref" , & object , & callback ) New in version 2.2. Changed in version 2.5: This function used an c_int type for min and max . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.Py_BuildValue.restype = POINTER(PyObject)
		dll.Py_BuildValue.argtypes = [ c_char_p, va_list ]
		dll.Py_BuildValue.__doc__ = """Return value: New reference. Create a new value based on a format string similar to those accepted by
	the PyArg_Parse*() family of functions and a sequence of values.
	Returns the value or NULL in the case of an error; an exception will be
	raised if NULL is returned. Py_BuildValue() does not always build a tuple.  It builds a tuple
	only if its format string contains two or more format units.  If the format
	string is empty, it returns None ; if it contains exactly one format
	unit, it returns whatever object is described by that format unit.  To
	force it to return a tuple of size 0 or one, parenthesize the format
	string. When memory buffers are passed as parameters to supply data to build
	objects, as for the s and s# formats, the required data is copied.
	Buffers provided by the caller are never referenced by the objects created
	by Py_BuildValue() .  In other words, if your code invokes malloc() and passes the allocated memory to Py_BuildValue() ,
	your code is responsible for calling free() for that memory once Py_BuildValue() returns. In the following description, the quoted form is the format unit; the entry
	in (round) parentheses is the Python object type that the format unit will
	return; and the entry in [square] brackets is the type of the C value(s) to
	be passed. The characters space, tab, colon and comma are ignored in format strings
	(but not within format units such as s# ).  This can be used to make
	long format strings a tad more readable. s (string) [char *] Convert a null-terminated C string to a Python object.  If the C string
	pointer is NULL , None is used. s# (string) [char *, c_int] Convert a C string and its length to a Python object.  If the C string
	pointer is NULL , the length is ignored and None is returned. z (string or None ) [char *] Same as s . z# (string or None ) [char *, c_int] Same as s# . u (Unicode string) [Py_UNICODE *] Convert a null-terminated buffer of Unicode (UCS-2 or UCS-4) data to a
	Python Unicode object.  If the Unicode buffer pointer is NULL , None is returned. u# (Unicode string) [Py_UNICODE *, c_int] Convert a Unicode (UCS-2 or UCS-4) data buffer and its length to a
	Python Unicode object.   If the Unicode buffer pointer is NULL , the
	length is ignored and None is returned. i (integer) [c_int] Convert a plain C c_int to a Python integer object. b (integer) [char] Convert a plain C char to a Python integer object. h (integer) [short c_int] Convert a plain C short c_int to a Python integer object. l (integer) [long c_int] Convert a C long c_int to a Python integer object. B (integer) [unsigned char] Convert a C unsigned char to a Python integer object. H (integer) [unsigned short c_int] Convert a C unsigned short c_int to a Python integer object. I (integer/long) [unsigned c_int] Convert a C unsigned c_int to a Python integer object or a Python
	long integer object, if it is larger than sys.maxint . k (integer/long) [unsigned long] Convert a C unsigned long to a Python integer object or a
	Python long integer object, if it is larger than sys.maxint . L (long) [PY_LONG_LONG] Convert a C long long to a Python long integer object. Only
	available on platforms that support long long . K (long) [unsigned PY_LONG_LONG] Convert a C unsigned long long to a Python long integer object.
	Only available on platforms that support unsigned long long . n (c_int) [Py_ssize_t] Convert a C Py_ssize_t to a Python integer or long integer. New in version 2.5. c (string of length 1) [char] Convert a C c_int representing a character to a Python string of
	length 1. d (float) [double] Convert a C double to a Python floating point number. f (float) [float] Same as d . D (complex) [Py_complex *] Convert a C Py_complex structure to a Python complex number. O (object) [PyObject *] Pass a Python object untouched (except for its reference count, which is
	incremented by one).  If the object passed in is a NULL pointer, it is
	assumed that this was caused because the call producing the argument
	found an error and set an exception. Therefore, Py_BuildValue() will return NULL but won't raise an exception.  If no exception has
	been raised yet, SystemError is set. S (object) [PyObject *] Same as O . N (object) [PyObject *] Same as O , except it doesn't increment the reference count on the
	object.  Useful when the object is created by a call to an object
	constructor in the argument list. O& (object) [ converter , anything ] Convert anything to a Python object through a converter function.
	The function is called with anything (which should be compatible with void * ) as its argument and should return a "new" Python
	object, or NULL if an error occurred. (items) (tuple) [ matching-items ] Convert a sequence of C values to a Python tuple with the same number of
	items. [items] (list) [ matching-items ] Convert a sequence of C values to a Python list with the same number of
	items. {items} (dictionary) [ matching-items ] Convert a sequence of C values to a Python dictionary.  Each pair of
	consecutive C values adds one item to the dictionary, serving as key and
	value, respectively. If there is an error in the format string, the SystemError exception
	is set and NULL returned."""
		dll._Py_BuildValue_SizeT.restype = POINTER(PyObject)
		dll._Py_BuildValue_SizeT.argtypes = [ c_char_p, va_list ]
		dll._PyArg_NoKeywords.restype = c_int
		dll._PyArg_NoKeywords.argtypes = [ c_char_p, POINTER(PyObject) ]
		dll.PyArg_VaParse.restype = c_int
		dll.PyArg_VaParse.argtypes = [ POINTER(PyObject), c_char_p, va_list ]
		dll.PyArg_VaParse.__doc__ = """Identical to PyArg_ParseTuple() , except that it accepts a va_list
	rather than a variable number of arguments."""
		dll.PyArg_VaParseTupleAndKeywords.restype = c_int
		dll.PyArg_VaParseTupleAndKeywords.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_char_p, POINTER(c_char_p), va_list ]
		dll.PyArg_VaParseTupleAndKeywords.__doc__ = """Identical to PyArg_ParseTupleAndKeywords() , except that it accepts a
	va_list rather than a variable number of arguments."""
		dll.Py_VaBuildValue.restype = POINTER(PyObject)
		dll.Py_VaBuildValue.argtypes = [ c_char_p, va_list ]
		dll.Py_VaBuildValue.__doc__ = """Identical to Py_BuildValue() , except that it accepts a va_list
	rather than a variable number of arguments."""
		dll.PyModule_AddObject.restype = c_int
		dll.PyModule_AddObject.argtypes = [ POINTER(PyObject), c_char_p, POINTER(PyObject) ]
		dll.PyModule_AddObject.__doc__ = """Add an object to module as name .  This is a convenience function which can
	be used from the module's initialization function.  This steals a reference to value .  Return -1 on error, 0 on success. New in version 2.0."""
		dll.PyModule_AddIntConstant.restype = c_int
		dll.PyModule_AddIntConstant.argtypes = [ POINTER(PyObject), c_char_p, c_long ]
		dll.PyModule_AddIntConstant.__doc__ = """Add an integer constant to module as name .  This convenience function can be
	used from the module's initialization function. Return -1 on error, 0 on
	success. New in version 2.0."""
		dll.PyModule_AddStringConstant.restype = c_int
		dll.PyModule_AddStringConstant.argtypes = [ POINTER(PyObject), c_char_p, c_char_p ]
		dll.PyModule_AddStringConstant.__doc__ = """Add a string constant to module as name .  This convenience function can be
	used from the module's initialization function.  The string value must be
	null-terminated.  Return -1 on error, 0 on success. New in version 2.0."""
		dll.Py_InitModule4.restype = POINTER(PyObject)
		dll.Py_InitModule4.argtypes = [ c_char_p, POINTER(py_object), c_char_p, POINTER(PyObject), c_int ]
		dll.Py_InitModule4.__doc__ = """Return value: Borrowed reference. Create a new module object based on a name and table of functions,
	returning the new module object.  If doc is non- NULL , it will be used
	to define the docstring for the module.  If self is non- NULL , it will
	passed to the functions of the module as their (otherwise NULL ) first
	parameter.  (This was added as an experimental feature, and there are no
	known uses in the current version of Python.)  For apiver , the only value
	which should be passed is defined by the constant PYTHON_API_VERSION . Note Most uses of this function should probably be using the Py_InitModule3() instead; only use this if you are sure you need
	it. Changed in version 2.3: Older versions of Python did not support NULL as the value for the methods argument."""
		dll.Py_SetProgramName.restype = None
		dll.Py_SetProgramName.argtypes = [ c_char_p ]
		dll.Py_SetProgramName.__doc__ = """This function should be called before Py_Initialize() is called for
	the first time, if it is called at all.  It tells the interpreter the value
	of the argv[0] argument to the main() function of the program.
	This is used by Py_GetPath() and some other functions below to find
	the Python run-time libraries relative to the interpreter executable.  The
	default value is 'python' .  The argument should point to a
	zero-terminated character string in static storage whose contents will not
	change for the duration of the program's execution.  No code in the Python
	interpreter will change the contents of this storage."""
		dll.Py_GetProgramName.restype = c_char_p
		dll.Py_GetProgramName.argtypes = [  ]
		dll.Py_GetProgramName.__doc__ = """Return the program name set with Py_SetProgramName() , or the default.
	The returned string points into static storage; the caller should not modify its
	value."""
		dll.Py_SetPythonHome.restype = None
		dll.Py_SetPythonHome.argtypes = [ c_char_p ]
		dll.Py_SetPythonHome.__doc__ = """Set the default "home" directory, that is, the location of the standard
	Python libraries.  See PYTHONHOME for the meaning of the
	argument string. The argument should point to a zero-terminated character string in static
	storage whose contents will not change for the duration of the program's
	execution.  No code in the Python interpreter will change the contents of
	this storage."""
		dll.Py_GetPythonHome.restype = c_char_p
		dll.Py_GetPythonHome.argtypes = [  ]
		dll.Py_GetPythonHome.__doc__ = """Return the default "home", that is, the value set by a previous call to Py_SetPythonHome() , or the value of the PYTHONHOME environment variable if it is set."""
		dll.Py_Initialize.restype = None
		dll.Py_Initialize.argtypes = [  ]
		dll.Py_Initialize.__doc__ = """Initialize the Python interpreter.  In an application embedding  Python, this
	should be called before using any other Python/C API functions; with the
	exception of Py_SetProgramName() , Py_SetPythonHome() , PyEval_InitThreads() , PyEval_ReleaseLock() , and PyEval_AcquireLock() . This initializes
	the table of loaded modules ( sys.modules ), and creates the fundamental
	modules __builtin__ , __main__ and sys .  It also initializes
	the module search path ( sys.path ). It does not set sys.argv ; use PySys_SetArgvEx() for that.  This is a no-op when called for a second time
	(without calling Py_Finalize() first).  There is no return value; it is a
	fatal error if the initialization fails."""
		dll.Py_InitializeEx.restype = None
		dll.Py_InitializeEx.argtypes = [ c_int ]
		dll.Py_InitializeEx.__doc__ = """This function works like Py_Initialize() if initsigs is 1. If initsigs is 0, it skips initialization registration of signal handlers, which
	might be useful when Python is embedded. New in version 2.4."""
		dll.Py_Finalize.restype = None
		dll.Py_Finalize.argtypes = [  ]
		dll.Py_Finalize.__doc__ = """Undo all initializations made by Py_Initialize() and subsequent use of
	Python/C API functions, and destroy all sub-interpreters (see Py_NewInterpreter() below) that were created and not yet destroyed since
	the last call to Py_Initialize() .  Ideally, this frees all memory
	allocated by the Python interpreter.  This is a no-op when called for a second
	time (without calling Py_Initialize() again first).  There is no return
	value; errors during finalization are ignored. This function is provided for a number of reasons.  An embedding application
	might want to restart Python without having to restart the application itself.
	An application that has loaded the Python interpreter from a dynamically
	loadable library (or DLL) might want to free all memory allocated by Python
	before unloading the DLL. During a hunt for memory leaks in an application a
	developer might want to free all memory allocated by Python before exiting from
	the application. Bugs and caveats: The destruction of modules and objects in modules is done
	in random order; this may cause destructors ( __del__() methods) to fail
	when they depend on other objects (even functions) or modules.  Dynamically
	loaded extension modules loaded by Python are not unloaded.  Small amounts of
	memory allocated by the Python interpreter may not be freed (if you find a leak,
	please report it).  Memory tied up in circular references between objects is not
	freed.  Some memory allocated by extension modules may not be freed.  Some
	extensions may not work properly if their initialization routine is called more
	than once; this can happen if an application calls Py_Initialize() and Py_Finalize() more than once."""
		dll.Py_IsInitialized.restype = c_int
		dll.Py_IsInitialized.argtypes = [  ]
		dll.Py_IsInitialized.__doc__ = """Return true (nonzero) when the Python interpreter has been initialized, false
	(zero) if not.  After Py_Finalize() is called, this returns false until Py_Initialize() is called again."""
		dll.Py_NewInterpreter.restype = POINTER(py_object)
		dll.Py_NewInterpreter.argtypes = [  ]
		dll.Py_NewInterpreter.__doc__ = """Create a new sub-interpreter.  This is an (almost) totally separate environment
	for the execution of Python code.  In particular, the new interpreter has
	separate, independent versions of all imported modules, including the
	fundamental modules builtins , __main__ and sys .  The
	table of loaded modules ( sys.modules ) and the module search path
	( sys.path ) are also separate.  The new environment has no sys.argv variable.  It has new standard I/O stream file objects sys.stdin , sys.stdout and sys.stderr (however these refer to the same underlying
	file descriptors). The return value points to the first thread state created in the new
	sub-interpreter.  This thread state is made in the current thread state.
	Note that no actual thread is created; see the discussion of thread states
	below.  If creation of the new interpreter is unsuccessful, NULL is
	returned; no exception is set since the exception state is stored in the
	current thread state and there may not be a current thread state.  (Like all
	other Python/C API functions, the global interpreter lock must be held before
	calling this function and is still held when it returns; however, unlike most
	other Python/C API functions, there needn't be a current thread state on
	entry.) Extension modules are shared between (sub-)interpreters as follows: the first
	time a particular extension is imported, it is initialized normally, and a
	(shallow) copy of its module's dictionary is squirreled away.  When the same
	extension is imported by another (sub-)interpreter, a new module is initialized
	and filled with the contents of this copy; the extension's init function is
	not called.  Note that this is different from what happens when an extension is
	imported after the interpreter has been completely re-initialized by calling Py_Finalize() and Py_Initialize() ; in that case, the extension's initmodule function is called again."""
		dll.Py_EndInterpreter.restype = None
		dll.Py_EndInterpreter.argtypes = [ POINTER(py_object) ]
		dll.Py_EndInterpreter.__doc__ = """Destroy the (sub-)interpreter represented by the given thread state. The given
	thread state must be the current thread state.  See the discussion of thread
	states below.  When the call returns, the current thread state is NULL .  All
	thread states associated with this interpreter are destroyed.  (The global
	interpreter lock must be held before calling this function and is still held
	when it returns.) Py_Finalize() will destroy all sub-interpreters that
	haven't been explicitly destroyed at that point."""
		dll.PyRun_AnyFileFlags.restype = c_int
		dll.PyRun_AnyFileFlags.argtypes = [ POINTER(FILE), c_char_p, POINTER(py_object) ]
		dll.PyRun_AnyFileFlags.__doc__ = """This is a simplified interface to PyRun_AnyFileExFlags() below, leaving
	the closeit argument set to 0 ."""
		dll.PyRun_AnyFileExFlags.restype = c_int
		dll.PyRun_AnyFileExFlags.argtypes = [ POINTER(FILE), c_char_p, c_int, POINTER(py_object) ]
		dll.PyRun_AnyFileExFlags.__doc__ = """If fp refers to a file associated with an interactive device (console or
	terminal input or Unix pseudo-terminal), return the value of PyRun_InteractiveLoop() , otherwise return the result of PyRun_SimpleFile() .  If filename is NULL , this function uses "???" as the filename."""
		dll.PyRun_SimpleStringFlags.restype = c_int
		dll.PyRun_SimpleStringFlags.argtypes = [ c_char_p, POINTER(py_object) ]
		dll.PyRun_SimpleStringFlags.__doc__ = """Executes the Python source code from command in the __main__ module
	according to the flags argument. If __main__ does not already exist, it
	is created.  Returns 0 on success or -1 if an exception was raised.  If
	there was an error, there is no way to get the exception information. For the
	meaning of flags , see below. Note that if an otherwise unhandled SystemExit is raised, this
	function will not return -1 , but exit the process, as long as Py_InspectFlag is not set."""
		dll.PyRun_SimpleFileExFlags.restype = c_int
		dll.PyRun_SimpleFileExFlags.argtypes = [ POINTER(FILE), c_char_p, c_int, POINTER(py_object) ]
		dll.PyRun_SimpleFileExFlags.__doc__ = """Similar to PyRun_SimpleStringFlags() , but the Python source code is read
	from fp instead of an in-memory string. filename should be the name of the
	file.  If closeit is true, the file is closed before PyRun_SimpleFileExFlags
	returns."""
		dll.PyRun_InteractiveOneFlags.restype = c_int
		dll.PyRun_InteractiveOneFlags.argtypes = [ POINTER(FILE), c_char_p, POINTER(py_object) ]
		dll.PyRun_InteractiveOneFlags.__doc__ = """Read and execute a single statement from a file associated with an
	interactive device according to the flags argument.  The user will be
	prompted using sys.ps1 and sys.ps2 .  Returns 0 when the input was
	executed successfully, -1 if there was an exception, or an error code
	from the errcode.h include file distributed as part of Python if
	there was a parse error.  (Note that errcode.h is not included by Python.h , so must be included specifically if needed.)"""
		dll.PyRun_InteractiveLoopFlags.restype = c_int
		dll.PyRun_InteractiveLoopFlags.argtypes = [ POINTER(FILE), c_char_p, POINTER(py_object) ]
		dll.PyRun_InteractiveLoopFlags.__doc__ = """Read and execute statements from a file associated with an interactive device
	until EOF is reached.  The user will be prompted using sys.ps1 and sys.ps2 .  Returns 0 at EOF."""
		dll.PyParser_ASTFromString.restype = POINTER(py_object)
		dll.PyParser_ASTFromString.argtypes = [ c_char_p, c_char_p, c_int, POINTER(py_object), POINTER(py_object) ]
		dll.PyParser_ASTFromFile.restype = POINTER(py_object)
		dll.PyParser_ASTFromFile.argtypes = [ POINTER(FILE), c_char_p, c_int, c_char_p, c_char_p, POINTER(py_object), POINTER(c_int), POINTER(py_object) ]
		dll.PyParser_SimpleParseStringFlags.restype = POINTER(py_object)
		dll.PyParser_SimpleParseStringFlags.argtypes = [ c_char_p, c_int, c_int ]
		dll.PyParser_SimpleParseStringFlags.__doc__ = """This is a simplified interface to PyParser_SimpleParseStringFlagsFilename() below, leaving filename set
	to NULL ."""
		dll.PyParser_SimpleParseFileFlags.restype = POINTER(py_object) #POINTER(struct _node)
		dll.PyParser_SimpleParseFileFlags.argtypes = [ POINTER(FILE), c_char_p, c_int, c_int ]
		dll.PyParser_SimpleParseFileFlags.__doc__ = """Similar to PyParser_SimpleParseStringFlagsFilename() , but the Python
	source code is read from fp instead of an in-memory string."""
		dll.PyRun_StringFlags.restype = POINTER(PyObject)
		dll.PyRun_StringFlags.argtypes = [ c_char_p, c_int, POINTER(PyObject), POINTER(PyObject), POINTER(py_object) ]
		dll.PyRun_StringFlags.__doc__ = """Return value: New reference. Execute Python source code from str in the context specified by the
	dictionaries globals and locals with the compiler flags specified by flags .  The parameter start specifies the start token that should be used to
	parse the source code. Returns the result of executing the code as a Python object, or NULL if an
	exception was raised."""
		dll.PyRun_FileExFlags.restype = POINTER(PyObject)
		dll.PyRun_FileExFlags.argtypes = [ POINTER(FILE), c_char_p, c_int, POINTER(PyObject), POINTER(PyObject), c_int, POINTER(py_object) ]
		dll.PyRun_FileExFlags.__doc__ = """Return value: New reference. Similar to PyRun_StringFlags() , but the Python source code is read from fp instead of an in-memory string. filename should be the name of the file.
	If closeit is true, the file is closed before PyRun_FileExFlags() returns."""
		dll.Py_CompileStringFlags.restype = POINTER(PyObject)
		dll.Py_CompileStringFlags.argtypes = [ c_char_p, c_char_p, c_int, POINTER(py_object) ]
		dll.Py_CompileStringFlags.__doc__ = """Return value: New reference. Parse and compile the Python source code in str , returning the resulting code
	object.  The start token is given by start ; this can be used to constrain the
	code which can be compiled and should be Py_eval_input , Py_file_input , or Py_single_input .  The filename specified by filename is used to construct the code object and may appear in tracebacks or SyntaxError exception messages.  This returns NULL if the code cannot
	be parsed or compiled."""
		dll.Py_SymtableString.restype = c_void_p #POINTER(struct symtable)
		dll.Py_SymtableString.argtypes = [ c_char_p, c_char_p, c_int ]
		dll.PyErr_Print.restype = None
		dll.PyErr_Print.argtypes = [  ]
		dll.PyErr_Print.__doc__ = """Alias for PyErr_PrintEx(1) ."""
		dll.PyErr_PrintEx.restype = None
		dll.PyErr_PrintEx.argtypes = [ c_int ]
		dll.PyErr_PrintEx.__doc__ = """Print a standard traceback to sys.stderr and clear the error indicator.
	Call this function only when the error indicator is set.  (Otherwise it will
	cause a fatal error!) If set_sys_last_vars is nonzero, the variables sys.last_type , sys.last_value and sys.last_traceback will be set to the
	type, value and traceback of the printed exception, respectively."""
		dll.PyErr_Display.restype = None
		dll.PyErr_Display.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.Py_AtExit.restype = c_int
		dll.Py_AtExit.argtypes = [ FARPROC ]
		dll.Py_AtExit.__doc__ = """Register a cleanup function to be called by Py_Finalize() .  The cleanup
	function will be called with no arguments and should return no value.  At most
	32 cleanup functions can be registered.  When the registration is successful, Py_AtExit() returns 0 ; on failure, it returns -1 .  The cleanup
	function registered last is called first. Each cleanup function will be called
	at most once.  Since Python's internal finalization will have completed before
	the cleanup function, no Python APIs should be called by func ."""
		dll.Py_Exit.restype = None
		dll.Py_Exit.argtypes = [ c_int ]
		dll.Py_Exit.__doc__ = """Exit the current process.  This calls Py_Finalize() and then calls the
	standard C library function exit(status) ."""
		dll.Py_FdIsInteractive.restype = c_int
		dll.Py_FdIsInteractive.argtypes = [ POINTER(FILE), c_char_p ]
		dll.Py_FdIsInteractive.__doc__ = """Return true (nonzero) if the standard I/O file fp with name filename is
	deemed interactive.  This is the case for files for which isatty(fileno(fp)) is true.  If the global flag Py_InteractiveFlag is true, this function
	also returns true if the filename pointer is NULL or if the name is equal to
	one of the strings '<stdin>' or '???' ."""
		dll.Py_Main.restype = c_int
		dll.Py_Main.argtypes = [ c_int, c_char_p * 1 ]
		dll.Py_Main.__doc__ = """The main program for the standard interpreter.  This is made available for
	programs which embed Python.  The argc and argv parameters should be
	prepared exactly as those which are passed to a C program's main() function.  It is important to note that the argument list may be modified (but
	the contents of the strings pointed to by the argument list are not). The return
	value will be 0 if the interpreter exits normally (ie, without an
	exception), 1 if the interpreter exits due to an exception, or 2 if the parameter list does not represent a valid Python command line. Note that if an otherwise unhandled SystemExit is raised, this
	function will not return 1 , but exit the process, as long as Py_InspectFlag is not set."""
		dll.Py_GetProgramFullPath.restype = c_char_p
		dll.Py_GetProgramFullPath.argtypes = [  ]
		dll.Py_GetProgramFullPath.__doc__ = """Return the full program name of the Python executable; this is  computed as a
	side-effect of deriving the default module search path  from the program name
	(set by Py_SetProgramName() above). The returned string points into
	static storage; the caller should not modify its value.  The value is available
	to Python code as sys.executable ."""
		dll.Py_GetPrefix.restype = c_char_p
		dll.Py_GetPrefix.argtypes = [  ]
		dll.Py_GetPrefix.__doc__ = """Return the prefix for installed platform-independent files. This is derived
	through a number of complicated rules from the program name set with Py_SetProgramName() and some environment variables; for example, if the
	program name is '/usr/local/bin/python' , the prefix is '/usr/local' . The
	returned string points into static storage; the caller should not modify its
	value.  This corresponds to the prefix variable in the top-level Makefile and the --prefix argument to the configure script at build time.  The value is available to Python code as sys.prefix .
	It is only useful on Unix.  See also the next function."""
		dll.Py_GetExecPrefix.restype = c_char_p
		dll.Py_GetExecPrefix.argtypes = [  ]
		dll.Py_GetExecPrefix.__doc__ = """Return the exec-prefix for installed platform- dependent files.  This is
	derived through a number of complicated rules from the program name set with Py_SetProgramName() and some environment variables; for example, if the
	program name is '/usr/local/bin/python' , the exec-prefix is '/usr/local' .  The returned string points into static storage; the caller
	should not modify its value.  This corresponds to the exec_prefix variable in the top-level Makefile and the --exec-prefix argument to the configure script at build  time.  The value is
	available to Python code as sys.exec_prefix .  It is only useful on Unix. Background: The exec-prefix differs from the prefix when platform dependent
	files (such as executables and shared libraries) are installed in a different
	directory tree.  In a typical installation, platform dependent files may be
	installed in the /usr/local/plat subtree while platform independent may
	be installed in /usr/local . Generally speaking, a platform is a combination of hardware and software
	families, e.g.  Sparc machines running the Solaris 2.x operating system are
	considered the same platform, but Intel machines running Solaris 2.x are another
	platform, and Intel machines running Linux are yet another platform.  Different
	major revisions of the same operating system generally also form different
	platforms.  Non-Unix operating systems are a different story; the installation
	strategies on those systems are so different that the prefix and exec-prefix are
	meaningless, and set to the empty string. Note that compiled Python bytecode
	files are platform independent (but not independent from the Python version by
	which they were compiled!). System administrators will know how to configure the mount or automount programs to share /usr/local between platforms
	while having /usr/local/plat be a different filesystem for each
	platform."""
		dll.Py_GetPath.restype = c_char_p
		dll.Py_GetPath.argtypes = [  ]
		dll.Py_GetPath.__doc__ = """Return the default module search path; this is computed from the program name
	(set by Py_SetProgramName() above) and some environment variables.
	The returned string consists of a series of directory names separated by a
	platform dependent delimiter character.  The delimiter character is ':' on Unix and Mac OS X, ';' on Windows.  The returned string points into
	static storage; the caller should not modify its value.  The list sys.path is initialized with this value on interpreter startup; it
	can be (and usually is) modified later to change the search path for loading
	modules."""
		dll.Py_GetVersion.restype = c_char_p
		dll.Py_GetVersion.argtypes = [  ]
		dll.Py_GetVersion.__doc__ = """Return the version of this Python interpreter.  This is a string that looks
	something like "1.5 (#67, Dec 31 1997, 22:34:28) [GCC 2.7.2.2]" The first word (up to the first space character) is the current Python version;
	the first three characters are the major and minor version separated by a
	period.  The returned string points into static storage; the caller should not
	modify its value.  The value is available to Python code as sys.version ."""
		dll.Py_GetPlatform.restype = c_char_p
		dll.Py_GetPlatform.argtypes = [  ]
		dll.Py_GetPlatform.__doc__ = """Return the platform identifier for the current platform.  On Unix, this is
	formed from the "official" name of the operating system, converted to lower
	case, followed by the major revision number; e.g., for Solaris 2.x, which is
	also known as SunOS 5.x, the value is 'sunos5' .  On Mac OS X, it is 'darwin' .  On Windows, it is 'win' .  The returned string points into
	static storage; the caller should not modify its value.  The value is available
	to Python code as sys.platform ."""
		dll.Py_GetCopyright.restype = c_char_p
		dll.Py_GetCopyright.argtypes = [  ]
		dll.Py_GetCopyright.__doc__ = """Return the official copyright string for the current Python version, for example 'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam' The returned string points into static storage; the caller should not modify its
	value.  The value is available to Python code as sys.copyright ."""
		dll.Py_GetCompiler.restype = c_char_p
		dll.Py_GetCompiler.argtypes = [  ]
		dll.Py_GetCompiler.__doc__ = """Return an indication of the compiler used to build the current Python version,
	in square brackets, for example: "[GCC 2.7.2.2]" The returned string points into static storage; the caller should not modify its
	value.  The value is available to Python code as part of the variable sys.version ."""
		dll.Py_GetBuildInfo.restype = c_char_p
		dll.Py_GetBuildInfo.argtypes = [  ]
		dll.Py_GetBuildInfo.__doc__ = """Return information about the sequence number and build date and time  of the
	current Python interpreter instance, for example "#67, Aug  1 1997, 22:34:28" The returned string points into static storage; the caller should not modify its
	value.  The value is available to Python code as part of the variable sys.version ."""
		dll._Py_svnversion.restype = c_char_p
		dll._Py_svnversion.argtypes = [  ]
		dll.Py_SubversionRevision.restype = c_char_p
		dll.Py_SubversionRevision.argtypes = [  ]
		dll.Py_SubversionShortBranch.restype = c_char_p
		dll.Py_SubversionShortBranch.argtypes = [  ]
		dll._Py_hgidentifier.restype = c_char_p
		dll._Py_hgidentifier.argtypes = [  ]
		dll._Py_hgversion.restype = c_char_p
		dll._Py_hgversion.argtypes = [  ]
		dll._PyBuiltin_Init.restype = POINTER(PyObject)
		dll._PyBuiltin_Init.argtypes = [  ]
		dll._PySys_Init.restype = POINTER(PyObject)
		dll._PySys_Init.argtypes = [  ]
		dll._PyImport_Init.restype = None
		dll._PyImport_Init.argtypes = [  ]
		dll._PyImport_Init.__doc__ = """Initialize the import mechanism.  For internal use only."""
		dll._PyExc_Init.restype = None
		dll._PyExc_Init.argtypes = [  ]
		dll._PyImportHooks_Init.restype = None
		dll._PyImportHooks_Init.argtypes = [  ]
		dll._PyFrame_Init.restype = c_int
		dll._PyFrame_Init.argtypes = [  ]
		dll._PyInt_Init.restype = c_int
		dll._PyInt_Init.argtypes = [  ]
		dll._PyLong_Init.restype = c_int
		dll._PyLong_Init.argtypes = [  ]
		dll._PyFloat_Init.restype = None
		dll._PyFloat_Init.argtypes = [  ]
		dll.PyByteArray_Init.restype = c_int
		dll.PyByteArray_Init.argtypes = [  ]
		dll._PyExc_Fini.restype = None
		dll._PyExc_Fini.argtypes = [  ]
		dll._PyImport_Fini.restype = None
		dll._PyImport_Fini.argtypes = [  ]
		dll._PyImport_Fini.__doc__ = """Finalize the import mechanism.  For internal use only."""
		dll.PyMethod_Fini.restype = None
		dll.PyMethod_Fini.argtypes = [  ]
		dll.PyFrame_Fini.restype = None
		dll.PyFrame_Fini.argtypes = [  ]
		dll.PyCFunction_Fini.restype = None
		dll.PyCFunction_Fini.argtypes = [  ]
		dll.PyDict_Fini.restype = None
		dll.PyDict_Fini.argtypes = [  ]
		dll.PyTuple_Fini.restype = None
		dll.PyTuple_Fini.argtypes = [  ]
		dll.PyList_Fini.restype = None
		dll.PyList_Fini.argtypes = [  ]
		dll.PySet_Fini.restype = None
		dll.PySet_Fini.argtypes = [  ]
		dll.PyString_Fini.restype = None
		dll.PyString_Fini.argtypes = [  ]
		dll.PyInt_Fini.restype = None
		dll.PyInt_Fini.argtypes = [  ]
		dll.PyFloat_Fini.restype = None
		dll.PyFloat_Fini.argtypes = [  ]
		dll.PyOS_FiniInterrupts.restype = None
		dll.PyOS_FiniInterrupts.argtypes = [  ]
		dll.PyByteArray_Fini.restype = None
		dll.PyByteArray_Fini.argtypes = [  ]
		dll.PyOS_Readline.restype = c_char_p
		dll.PyOS_Readline.argtypes = [ POINTER(FILE), POINTER(FILE), c_char_p ]
		dll.PyOS_CheckStack.restype = c_int
		dll.PyOS_CheckStack.argtypes = [  ]
		dll.PyOS_CheckStack.__doc__ = """Return true when the interpreter runs out of stack space.  This is a reliable
	check, but is only available when USE_STACKCHECK is defined (currently
	on Windows using the Microsoft Visual C++ compiler). USE_STACKCHECK will be defined automatically; you should never change the definition in your
	own code."""
		dll.PyOS_getsig.restype = py_object
		dll.PyOS_getsig.argtypes = [ c_int ]
		dll.PyOS_getsig.__doc__ = """Return the current signal handler for signal i .  This is a thin wrapper around
	either sigaction() or signal() .  Do not call those functions
	directly! PyOS_sighandler_t is a typedef alias for void (*)(c_int) ."""
		dll.PyOS_setsig.restype = py_object
		dll.PyOS_setsig.argtypes = [ c_int, py_object ]
		dll.PyOS_setsig.__doc__ = """Set the signal handler for signal i to be h ; return the old signal handler.
	This is a thin wrapper around either sigaction() or signal() .  Do
	not call those functions directly! PyOS_sighandler_t is a typedef
	alias for void (*)(c_int) ."""
		dll.PyEval_CallObjectWithKeywords.restype = POINTER(PyObject)
		dll.PyEval_CallObjectWithKeywords.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyEval_CallFunction.restype = POINTER(PyObject)
		dll.PyEval_CallFunction.argtypes = [ POINTER(PyObject), c_char_p, va_list ]
		dll.PyEval_CallMethod.restype = POINTER(PyObject)
		dll.PyEval_CallMethod.argtypes = [ POINTER(PyObject), c_char_p, c_char_p, va_list ]
		dll.PyEval_SetProfile.restype = None
		dll.PyEval_SetProfile.argtypes = [ py_object, POINTER(PyObject) ]
		dll.PyEval_SetProfile.__doc__ = """Set the profiler function to func .  The obj parameter is passed to the
	function as its first parameter, and may be any Python object, or NULL .  If
	the profile function needs to maintain state, using a different value for obj for each thread provides a convenient and thread-safe place to store it.  The
	profile function is called for all monitored events except the line-number
	events."""
		dll.PyEval_SetTrace.restype = None
		dll.PyEval_SetTrace.argtypes = [ py_object, POINTER(PyObject) ]
		dll.PyEval_SetTrace.__doc__ = """Set the tracing function to func .  This is similar to PyEval_SetProfile() , except the tracing function does receive line-number
	events."""
		dll.PyEval_GetBuiltins.restype = POINTER(PyObject)
		dll.PyEval_GetBuiltins.argtypes = [  ]
		dll.PyEval_GetBuiltins.__doc__ = """Return value: Borrowed reference. Return a dictionary of the builtins in the current execution frame,
	or the interpreter of the thread state if no frame is currently executing."""
		dll.PyEval_GetGlobals.restype = POINTER(PyObject)
		dll.PyEval_GetGlobals.argtypes = [  ]
		dll.PyEval_GetGlobals.__doc__ = """Return value: Borrowed reference. Return a dictionary of the global variables in the current execution frame,
	or NULL if no frame is currently executing."""
		dll.PyEval_GetLocals.restype = POINTER(PyObject)
		dll.PyEval_GetLocals.argtypes = [  ]
		dll.PyEval_GetLocals.__doc__ = """Return value: Borrowed reference. Return a dictionary of the local variables in the current execution frame,
	or NULL if no frame is currently executing."""
		dll.PyEval_GetFrame.restype = c_void_p #POINTER(struct _frame)
		dll.PyEval_GetFrame.argtypes = [  ]
		dll.PyEval_GetFrame.__doc__ = """Return value: Borrowed reference. Return the current thread state's frame, which is NULL if no frame is
	currently executing."""
		dll.PyEval_GetRestricted.restype = c_int
		dll.PyEval_GetRestricted.argtypes = [  ]
		dll.PyEval_GetRestricted.__doc__ = """If there is a current frame and it is executing in restricted mode, return true,
	otherwise false."""
		dll.PyEval_MergeCompilerFlags.restype = c_int
		dll.PyEval_MergeCompilerFlags.argtypes = [ POINTER(py_object) ]
		dll.PyEval_MergeCompilerFlags.__doc__ = """This function changes the flags of the current evaluation frame, and returns
	true on success, false on failure."""
		dll.Py_FlushLine.restype = c_int
		dll.Py_FlushLine.argtypes = [  ]
		dll.Py_AddPendingCall.restype = c_int
		dll.Py_AddPendingCall.argtypes = [ CFUNCTYPE(c_int, (c_void_p,)), c_void_p ]
		dll.Py_AddPendingCall.__doc__ = """Post a notification to the Python main thread.  If successful, func will be
	called with the argument arg at the earliest convenience. func will be
	called having the global interpreter lock held and can thus use the full
	Python API and can take any action such as setting object attributes to
	signal IO completion.  It must return 0 on success, or -1 signalling an
	exception.  The notification function won't be interrupted to perform another
	asynchronous notification recursively, but it can still be interrupted to
	switch threads if the global interpreter lock is released, for example, if it
	calls back into Python code. This function returns 0 on success in which case the notification has been
	scheduled.  Otherwise, for example if the notification buffer is full, it
	returns -1 without setting any exception. This function can be called on any thread, be it a Python thread or some
	other system thread.  If it is a Python thread, it doesn't matter if it holds
	the global interpreter lock or not. New in version 2.7."""
		dll.Py_MakePendingCalls.restype = c_int
		dll.Py_MakePendingCalls.argtypes = [  ]
		dll.Py_SetRecursionLimit.restype = None
		dll.Py_SetRecursionLimit.argtypes = [ c_int ]
		dll.Py_GetRecursionLimit.restype = c_int
		dll.Py_GetRecursionLimit.argtypes = [  ]
		dll._Py_CheckRecursiveCall.restype = c_int
		dll._Py_CheckRecursiveCall.argtypes = [ c_char_p ]
		dll.PyEval_GetFuncName.restype = c_char_p
		dll.PyEval_GetFuncName.argtypes = [ POINTER(PyObject) ]
		dll.PyEval_GetFuncName.__doc__ = """Return the name of func if it is a function, class or instance object, else the
	name of func s type."""
		dll.PyEval_GetFuncDesc.restype = c_char_p
		dll.PyEval_GetFuncDesc.argtypes = [ POINTER(PyObject) ]
		dll.PyEval_GetFuncDesc.__doc__ = """Return a description string, depending on the type of func .
	Return values include "()" for functions and methods, " constructor",
	" instance", and " object".  Concatenated with the result of PyEval_GetFuncName() , the result will be a description of func ."""
		dll.PyEval_GetCallStats.restype = POINTER(PyObject)
		dll.PyEval_GetCallStats.argtypes = [ POINTER(PyObject) ]
		dll.PyEval_GetCallStats.__doc__ = """Return a tuple of function call counts.  There are constants defined for the
	positions within the tuple: Name Value PCALL_ALL 0 PCALL_FUNCTION 1 PCALL_FAST_FUNCTION 2 PCALL_FASTER_FUNCTION 3 PCALL_METHOD 4 PCALL_BOUND_METHOD 5 PCALL_CFUNCTION 6 PCALL_TYPE 7 PCALL_GENERATOR 8 PCALL_OTHER 9 PCALL_POP 10 PCALL_FAST_FUNCTION means no argument tuple needs to be created. PCALL_FASTER_FUNCTION means that the fast-path frame setup code is used. If there is a method call where the call can be optimized by changing
	the argument tuple and calling the function directly, it gets recorded
	twice. This function is only present if Python is compiled with CALL_PROFILE defined."""
		dll.PyEval_EvalFrame.restype = POINTER(PyObject)
		dll.PyEval_EvalFrame.argtypes = [ c_void_p ] # POINTER(struct _frame)
		dll.PyEval_EvalFrame.__doc__ = """Evaluate an execution frame.  This is a simplified interface to
	PyEval_EvalFrameEx, for backward compatibility."""
		dll.PyEval_EvalFrameEx.restype = POINTER(PyObject)
		dll.PyEval_EvalFrameEx.argtypes = [ c_void_p, c_int ] # POINTER(struct _frame)
		dll.PyEval_EvalFrameEx.__doc__ = """This is the main, unvarnished function of Python interpretation.  It is
	literally 2000 lines long.  The code object associated with the execution
	frame f is executed, interpreting bytecode and executing calls as needed.
	The additional throwflag parameter can mostly be ignored - if true, then
	it causes an exception to immediately be thrown; this is used for the throw() methods of generator objects."""
		dll.PyEval_SaveThread.restype = POINTER(py_object)
		dll.PyEval_SaveThread.argtypes = [  ]
		dll.PyEval_SaveThread.__doc__ = """Release the global interpreter lock (if it has been created and thread
	support is enabled) and reset the thread state to NULL , returning the
	previous thread state (which is not NULL ).  If the lock has been created,
	the current thread must have acquired it.  (This function is available even
	when thread support is disabled at compile time.)"""
		dll.PyEval_RestoreThread.restype = None
		dll.PyEval_RestoreThread.argtypes = [ POINTER(py_object) ]
		dll.PyEval_RestoreThread.__doc__ = """Acquire the global interpreter lock (if it has been created and thread
	support is enabled) and set the thread state to tstate , which must not be NULL .  If the lock has been created, the current thread must not have
	acquired it, otherwise deadlock ensues.  (This function is available even
	when thread support is disabled at compile time.)"""
		dll.PyEval_ThreadsInitialized.restype = c_int
		dll.PyEval_ThreadsInitialized.argtypes = [  ]
		dll.PyEval_ThreadsInitialized.__doc__ = """Returns a non-zero value if PyEval_InitThreads() has been called.  This
	function can be called without holding the GIL, and therefore can be used to
	avoid calls to the locking API when running single-threaded.  This function is
	not available when thread support is disabled at compile time. New in version 2.4."""
		dll.PyEval_InitThreads.restype = None
		dll.PyEval_InitThreads.argtypes = [  ]
		dll.PyEval_InitThreads.__doc__ = """Initialize and acquire the global interpreter lock.  It should be called in the
	main thread before creating a second thread or engaging in any other thread
	operations such as PyEval_ReleaseLock() or PyEval_ReleaseThread(tstate) . It is not needed before calling PyEval_SaveThread() or PyEval_RestoreThread() . This is a no-op when called for a second time.  It is safe to call this function
	before calling Py_Initialize() . Note When only the main thread exists, no GIL operations are needed. This is a
	common situation (most Python programs do not use threads), and the lock
	operations slow the interpreter down a bit. Therefore, the lock is not
	created initially.  This situation is equivalent to having acquired the lock:
	when there is only a single thread, all object accesses are safe.  Therefore,
	when this function initializes the global interpreter lock, it also acquires
	it.  Before the Python _thread module creates a new thread, knowing
	that either it has the lock or the lock hasn't been created yet, it calls PyEval_InitThreads() .  When this call returns, it is guaranteed that
	the lock has been created and that the calling thread has acquired it. It is not safe to call this function when it is unknown which thread (if
	any) currently has the global interpreter lock. This function is not available when thread support is disabled at compile time."""
		dll.PyEval_AcquireLock.restype = None
		dll.PyEval_AcquireLock.argtypes = [  ]
		dll.PyEval_AcquireLock.__doc__ = """Acquire the global interpreter lock.  The lock must have been created earlier.
	If this thread already has the lock, a deadlock ensues. Warning This function does not change the current thread state.  Please use PyEval_RestoreThread() or PyEval_AcquireThread() instead."""
		dll.PyEval_ReleaseLock.restype = None
		dll.PyEval_ReleaseLock.argtypes = [  ]
		dll.PyEval_ReleaseLock.__doc__ = """Release the global interpreter lock.  The lock must have been created earlier. Warning This function does not change the current thread state.  Please use PyEval_SaveThread() or PyEval_ReleaseThread() instead."""
		dll.PyEval_AcquireThread.restype = None
		dll.PyEval_AcquireThread.argtypes = [ POINTER(py_object) ]
		dll.PyEval_AcquireThread.__doc__ = """Acquire the global interpreter lock and set the current thread state to tstate , which should not be NULL .  The lock must have been created earlier.
	If this thread already has the lock, deadlock ensues. PyEval_RestoreThread() is a higher-level function which is always
	available (even when thread support isn't enabled or when threads have
	not been initialized)."""
		dll.PyEval_ReleaseThread.restype = None
		dll.PyEval_ReleaseThread.argtypes = [ POINTER(py_object) ]
		dll.PyEval_ReleaseThread.__doc__ = """Reset the current thread state to NULL and release the global interpreter
	lock.  The lock must have been created earlier and must be held by the current
	thread.  The tstate argument, which must not be NULL , is only used to check
	that it represents the current thread state - if it isn't, a fatal error is
	reported. PyEval_SaveThread() is a higher-level function which is always
	available (even when thread support isn't enabled or when threads have
	not been initialized)."""
		dll.PyEval_ReInitThreads.restype = None
		dll.PyEval_ReInitThreads.argtypes = [  ]
		dll.PyEval_ReInitThreads.__doc__ = """This function is called from PyOS_AfterFork() to ensure that newly
	created child processes don't hold locks referring to threads which
	are not running in the child process."""
		dll._PyEval_SliceIndex.restype = c_int
		dll._PyEval_SliceIndex.argtypes = [ POINTER(PyObject), POINTER(c_ssize_t) ]
		dll.PySys_GetObject.restype = POINTER(PyObject)
		dll.PySys_GetObject.argtypes = [ c_char_p ]
		dll.PySys_GetObject.__doc__ = """Return value: Borrowed reference. Return the object name from the sys module or NULL if it does
	not exist, without setting an exception."""
		dll.PySys_SetObject.restype = c_int
		dll.PySys_SetObject.argtypes = [ c_char_p, POINTER(PyObject) ]
		dll.PySys_SetObject.__doc__ = """Set name in the sys module to v unless v is NULL , in which
	case name is deleted from the sys module. Returns 0 on success, -1 on error."""
		dll.PySys_GetFile.restype = POINTER(FILE)
		dll.PySys_GetFile.argtypes = [ c_char_p, POINTER(FILE) ]
		dll.PySys_GetFile.__doc__ = """Return the FILE* associated with the object name in the sys module, or def if name is not in the module or is not associated
	with a FILE* ."""
		dll.PySys_SetArgv.restype = None
		dll.PySys_SetArgv.argtypes = [ c_int, POINTER(c_char_p) ]
		dll.PySys_SetArgv.__doc__ = """This function works like PySys_SetArgvEx() with updatepath set to 1."""
		dll.PySys_SetArgvEx.restype = None
		dll.PySys_SetArgvEx.argtypes = [ c_int, POINTER(c_char_p), c_int ]
		dll.PySys_SetArgvEx.__doc__ = """Set sys.argv based on argc and argv .  These parameters are
	similar to those passed to the program's main() function with the
	difference that the first entry should refer to the script file to be
	executed rather than the executable hosting the Python interpreter.  If there
	isn't a script that will be run, the first entry in argv can be an empty
	string.  If this function fails to initialize sys.argv , a fatal
	condition is signalled using Py_FatalError() . If updatepath is zero, this is all the function does.  If updatepath is non-zero, the function also modifies sys.path according to the
	following algorithm: If the name of an existing script is passed in argv[0] , the absolute
	path of the directory where the script is located is prepended to sys.path . Otherwise (that is, if argc is 0 or argv[0] doesn't point
	to an existing file name), an empty string is prepended to sys.path , which is the same as prepending the current working
	directory ( "." ). Note It is recommended that applications embedding the Python interpreter
	for purposes other than executing a single script pass 0 as updatepath ,
	and update sys.path themselves if desired.
	See CVE-2008-5983 . On versions before 2.6.6, you can achieve the same effect by manually
	popping the first sys.path element after having called PySys_SetArgv() , for example using: PyRun_SimpleString ( "import sys; sys.path.pop(0) \\n " ); New in version 2.6.6."""
		dll.PySys_SetPath.restype = None
		dll.PySys_SetPath.argtypes = [ c_char_p ]
		dll.PySys_SetPath.__doc__ = """Set sys.path to a list object of paths found in path which should
	be a list of paths separated with the platform's search path delimiter
	( : on Unix, ; on Windows)."""
		dll.PySys_ResetWarnOptions.restype = None
		dll.PySys_ResetWarnOptions.argtypes = [  ]
		dll.PySys_ResetWarnOptions.__doc__ = """Reset sys.warnoptions to an empty list."""
		dll.PySys_AddWarnOption.restype = None
		dll.PySys_AddWarnOption.argtypes = [ c_char_p ]
		dll.PySys_AddWarnOption.__doc__ = """Append s to sys.warnoptions ."""
		dll.PySys_HasWarnOptions.restype = c_int
		dll.PySys_HasWarnOptions.argtypes = [  ]
		dll.PyOS_InterruptOccurred.restype = c_int
		dll.PyOS_InterruptOccurred.argtypes = [  ]
		dll.PyOS_InitInterrupts.restype = None
		dll.PyOS_InitInterrupts.argtypes = [  ]
		dll.PyOS_AfterFork.restype = None
		dll.PyOS_AfterFork.argtypes = [  ]
		dll.PyOS_AfterFork.__doc__ = """Function to update some internal state after a process fork; this should be
	called in the new process if the Python interpreter will continue to be used.
	If a new executable is loaded into the new process, this function does not need
	to be called."""
		dll.PyImport_GetMagicNumber.restype = c_long
		dll.PyImport_GetMagicNumber.argtypes = [  ]
		dll.PyImport_GetMagicNumber.__doc__ = """Return the magic number for Python bytecode files (a.k.a. .pyc and .pyo files).  The magic number should be present in the first four bytes
	of the bytecode file, in little-endian byte order."""
		dll.PyImport_ExecCodeModule.restype = POINTER(PyObject)
		dll.PyImport_ExecCodeModule.argtypes = [ c_char_p, POINTER(PyObject) ]
		dll.PyImport_ExecCodeModule.__doc__ = """Return value: New reference. Given a module name (possibly of the form package.module ) and a code object
	read from a Python bytecode file or obtained from the built-in function compile() , load the module.  Return a new reference to the module object,
	or NULL with an exception set if an error occurred.  Before Python 2.4, the
	module could still be created in error cases.  Starting with Python 2.4, name is removed from sys.modules in error cases, and even if name was already
	in sys.modules on entry to PyImport_ExecCodeModule() .  Leaving
	incompletely initialized modules in sys.modules is dangerous, as imports of
	such modules have no way to know that the module object is an unknown (and
	probably damaged with respect to the module author's intents) state. The module's __file__ attribute will be set to the code object's co_filename . This function will reload the module if it was already imported.  See PyImport_ReloadModule() for the intended way to reload a module. If name points to a dotted name of the form package.module , any package
	structures not already created will still not be created. Changed in version 2.4: name is removed from sys.modules in error cases."""
		dll.PyImport_ExecCodeModuleEx.restype = POINTER(PyObject)
		dll.PyImport_ExecCodeModuleEx.argtypes = [ c_char_p, POINTER(PyObject), c_char_p ]
		dll.PyImport_ExecCodeModuleEx.__doc__ = """Return value: New reference. Like PyImport_ExecCodeModule() , but the __file__ attribute of
	the module object is set to pathname if it is non- NULL ."""
		dll.PyImport_GetModuleDict.restype = POINTER(PyObject)
		dll.PyImport_GetModuleDict.argtypes = [  ]
		dll.PyImport_GetModuleDict.__doc__ = """Return value: Borrowed reference. Return the dictionary used for the module administration (a.k.a. sys.modules ).  Note that this is a per-interpreter variable."""
		dll.PyImport_AddModule.restype = POINTER(PyObject)
		dll.PyImport_AddModule.argtypes = [ c_char_p ]
		dll.PyImport_AddModule.__doc__ = """Return value: Borrowed reference. Return the module object corresponding to a module name.  The name argument
	may be of the form package.module . First check the modules dictionary if
	there's one there, and if not, create a new one and insert it in the modules
	dictionary. Return NULL with an exception set on failure. Note This function does not load or import the module; if the module wasn't already
	loaded, you will get an empty module object. Use PyImport_ImportModule() or one of its variants to import a module.  Package structures implied by a
	dotted name for name are not created if not already present."""
		dll.PyImport_ImportModule.restype = POINTER(PyObject)
		dll.PyImport_ImportModule.argtypes = [ c_char_p ]
		dll.PyImport_ImportModule.__doc__ = """Return value: New reference. This is a simplified interface to PyImport_ImportModuleEx() below,
	leaving the globals and locals arguments set to NULL and level set
	to 0.  When the name argument contains a dot (when it specifies a submodule of a package), the fromlist argument is set to the list ['*'] so that the return value is the
	named module rather than the top-level package containing it as would otherwise
	be the case.  (Unfortunately, this has an additional side effect when name in
	fact specifies a subpackage instead of a submodule: the submodules specified in
	the package's __all__ variable are  loaded.)  Return a new reference to the
	imported module, or NULL with an exception set on failure.  Before Python 2.4,
	the module may still be created in the failure case - examine sys.modules to find out.  Starting with Python 2.4, a failing import of a module no longer
	leaves the module in sys.modules . Changed in version 2.4: Failing imports remove incomplete module objects. Changed in version 2.6: Always uses absolute imports."""
		dll.PyImport_ImportModuleNoBlock.restype = POINTER(PyObject)
		dll.PyImport_ImportModuleNoBlock.argtypes = [ c_char_p ]
		dll.PyImport_ImportModuleNoBlock.__doc__ = """This version of PyImport_ImportModule() does not block. It's intended
	to be used in C functions that import other modules to execute a function.
	The import may block if another thread holds the import lock. The function PyImport_ImportModuleNoBlock() never blocks. It first tries to fetch
	the module from sys.modules and falls back to PyImport_ImportModule() unless the lock is held, in which case the function will raise an ImportError . New in version 2.6."""
		dll.PyImport_ImportModuleLevel.restype = POINTER(PyObject)
		dll.PyImport_ImportModuleLevel.argtypes = [ c_char_p, POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), c_int ]
		dll.PyImport_ImportModuleLevel.__doc__ = """Return value: New reference. Import a module.  This is best described by referring to the built-in Python
	function __import__() , as the standard __import__() function calls
	this function directly. The return value is a new reference to the imported module or top-level package,
	or NULL with an exception set on failure.  Like for __import__() ,
	the return value when a submodule of a package was requested is normally the
	top-level package, unless a non-empty fromlist was given. New in version 2.5."""
		dll.PyImport_GetImporter.restype = POINTER(PyObject)
		dll.PyImport_GetImporter.argtypes = [ POINTER(PyObject) ]
		dll.PyImport_GetImporter.__doc__ = """Return an importer object for a sys.path / pkg.__path__ item path , possibly by fetching it from the sys.path_importer_cache dict.  If it wasn't yet cached, traverse sys.path_hooks until a hook
	is found that can handle the path item.  Return None if no hook could;
	this tells our caller it should fall back to the built-in import mechanism.
	Cache the result in sys.path_importer_cache .  Return a new reference
	to the importer object. New in version 2.6."""
		dll.PyImport_Import.restype = POINTER(PyObject)
		dll.PyImport_Import.argtypes = [ POINTER(PyObject) ]
		dll.PyImport_Import.__doc__ = """Return value: New reference. This is a higher-level interface that calls the current "import hook function".
	It invokes the __import__() function from the __builtins__ of the
	current globals.  This means that the import is done using whatever import hooks
	are installed in the current environment, e.g. by rexec or ihooks . Changed in version 2.6: Always uses absolute imports."""
		dll.PyImport_ReloadModule.restype = POINTER(PyObject)
		dll.PyImport_ReloadModule.argtypes = [ POINTER(PyObject) ]
		dll.PyImport_ReloadModule.__doc__ = """Return value: New reference. Reload a module.  This is best described by referring to the built-in Python
	function reload() , as the standard reload() function calls this
	function directly.  Return a new reference to the reloaded module, or NULL with an exception set on failure (the module still exists in this case)."""
		dll.PyImport_Cleanup.restype = None
		dll.PyImport_Cleanup.argtypes = [  ]
		dll.PyImport_Cleanup.__doc__ = """Empty the module table.  For internal use only."""
		dll.PyImport_ImportFrozenModule.restype = c_int
		dll.PyImport_ImportFrozenModule.argtypes = [ c_char_p ]
		dll.PyImport_ImportFrozenModule.__doc__ = """Load a frozen module named name .  Return 1 for success, 0 if the
	module is not found, and -1 with an exception set if the initialization
	failed.  To access the imported module on a successful load, use PyImport_ImportModule() .  (Note the misnomer - this function would
	reload the module if it was already imported.)"""
		dll._PyImport_AcquireLock.restype = None
		dll._PyImport_AcquireLock.argtypes = [  ]
		dll._PyImport_ReleaseLock.restype = c_int
		dll._PyImport_ReleaseLock.argtypes = [  ]
		dll._PyImport_FindModule.restype = c_void_p # POINTER(struct filedescr)
		dll._PyImport_FindModule.argtypes = [ c_char_p, POINTER(PyObject), c_char_p, c_size_t, POINTER(POINTER(FILE)), POINTER(POINTER(PyObject)) ]
		dll._PyImport_IsScript.restype = c_int
		dll._PyImport_IsScript.argtypes = [ c_void_p ] # POINTER(struct filedescr)
		dll._PyImport_ReInitLock.restype = None
		dll._PyImport_ReInitLock.argtypes = [  ]
		dll._PyImport_FindExtension.restype = POINTER(PyObject)
		dll._PyImport_FindExtension.argtypes = [ c_char_p, c_char_p ]
		dll._PyImport_FindExtension.__doc__ = """For internal use only."""
		dll._PyImport_FixupExtension.restype = POINTER(PyObject)
		dll._PyImport_FixupExtension.argtypes = [ c_char_p, c_char_p ]
		dll._PyImport_FixupExtension.__doc__ = """For internal use only."""
		dll.PyImport_AppendInittab.restype = c_int
		dll.PyImport_AppendInittab.argtypes = [ c_char_p, FARPROC ]
		dll.PyImport_AppendInittab.__doc__ = """Add a single module to the existing table of built-in modules.  This is a
	convenience wrapper around PyImport_ExtendInittab() , returning -1 if
	the table could not be extended.  The new module can be imported by the name name , and uses the function initfunc as the initialization function called
	on the first attempted import.  This should be called before Py_Initialize() ."""
		dll.PyImport_ExtendInittab.restype = c_int
		dll.PyImport_ExtendInittab.argtypes = [ c_void_p ] # POINTER(struct _inittab)
		dll.PyImport_ExtendInittab.__doc__ = """Add a collection of modules to the table of built-in modules.  The newtab array must end with a sentinel entry which contains NULL for the name field; failure to provide the sentinel value can result in a memory fault.
	Returns 0 on success or -1 if insufficient memory could be allocated to
	extend the internal table.  In the event of failure, no modules are added to the
	internal table.  This should be called before Py_Initialize() ."""
		dll.PyObject_Cmp.restype = c_int
		dll.PyObject_Cmp.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(c_int) ]
		dll.PyObject_Cmp.__doc__ = """Compare the values of o1 and o2 using a routine provided by o1 , if one
	exists, otherwise with a routine provided by o2 .  The result of the comparison
	is returned in result .  Returns -1 on failure.  This is the equivalent of
	the Python statement result = cmp(o1, o2) ."""
		dll.PyObject_Call.restype = POINTER(PyObject)
		dll.PyObject_Call.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_Call.__doc__ = """Return value: New reference. Call a callable Python object callable_object , with arguments given by the
	tuple args , and named arguments given by the dictionary kw . If no named
	arguments are needed, kw may be NULL . args must not be NULL , use an
	empty tuple if no arguments are needed. Returns the result of the call on
	success, or NULL on failure.  This is the equivalent of the Python expression apply(callable_object, args, kw) or callable_object(*args, **kw) . New in version 2.2."""
		dll.PyObject_CallObject.restype = POINTER(PyObject)
		dll.PyObject_CallObject.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_CallObject.__doc__ = """Return value: New reference. Call a callable Python object callable_object , with arguments given by the
	tuple args .  If no arguments are needed, then args may be NULL .  Returns
	the result of the call on success, or NULL on failure.  This is the equivalent
	of the Python expression apply(callable_object, args) or callable_object(*args) ."""
		dll.PyObject_CallFunction.restype = POINTER(PyObject)
		dll.PyObject_CallFunction.argtypes = [ POINTER(PyObject), c_char_p, va_list ]
		dll.PyObject_CallFunction.__doc__ = """Return value: New reference. Call a callable Python object callable , with a variable number of C arguments.
	The C arguments are described using a Py_BuildValue() style format
	string.  The format may be NULL , indicating that no arguments are provided.
	Returns the result of the call on success, or NULL on failure.  This is the
	equivalent of the Python expression apply(callable, args) or callable(*args) . Note that if you only pass PyObject * args, PyObject_CallFunctionObjArgs() is a faster alternative."""
		dll.PyObject_CallMethod.restype = POINTER(PyObject)
		dll.PyObject_CallMethod.argtypes = [ POINTER(PyObject), c_char_p, c_char_p, va_list ]
		dll.PyObject_CallMethod.__doc__ = """Return value: New reference. Call the method named method of object o with a variable number of C
	arguments.  The C arguments are described by a Py_BuildValue() format
	string that should  produce a tuple.  The format may be NULL , indicating that
	no arguments are provided. Returns the result of the call on success, or NULL on failure.  This is the equivalent of the Python expression o.method(args) .
	Note that if you only pass PyObject * args, PyObject_CallMethodObjArgs() is a faster alternative."""
		dll._PyObject_CallFunction_SizeT.restype = POINTER(PyObject)
		dll._PyObject_CallFunction_SizeT.argtypes = [ POINTER(PyObject), c_char_p, va_list ]
		dll._PyObject_CallMethod_SizeT.restype = POINTER(PyObject)
		dll._PyObject_CallMethod_SizeT.argtypes = [ POINTER(PyObject), c_char_p, c_char_p, va_list ]
		dll.PyObject_CallFunctionObjArgs.restype = POINTER(PyObject)
		dll.PyObject_CallFunctionObjArgs.argtypes = [ POINTER(PyObject), va_list ]
		dll.PyObject_CallFunctionObjArgs.__doc__ = """Return value: New reference. Call a callable Python object callable , with a variable number of PyObject* arguments.  The arguments are provided as a variable number
	of parameters followed by NULL . Returns the result of the call on success, or NULL on failure. New in version 2.2."""
		dll.PyObject_CallMethodObjArgs.restype = POINTER(PyObject)
		dll.PyObject_CallMethodObjArgs.argtypes = [ POINTER(PyObject), POINTER(PyObject), va_list ]
		dll.PyObject_CallMethodObjArgs.__doc__ = """Return value: New reference. Calls a method of the object o , where the name of the method is given as a
	Python string object in name .  It is called with a variable number of PyObject* arguments.  The arguments are provided as a variable number
	of parameters followed by NULL . Returns the result of the call on success, or NULL on failure. New in version 2.2."""
		dll.PyObject_Type.restype = POINTER(PyObject)
		dll.PyObject_Type.argtypes = [ POINTER(PyObject) ]
		dll.PyObject_Type.__doc__ = """Return value: New reference. When o is non- NULL , returns a type object corresponding to the object type
	of object o . On failure, raises SystemError and returns NULL .  This
	is equivalent to the Python expression type(o) . This function increments the
	reference count of the return value. There's really no reason to use this
	function instead of the common expression o->ob_type , which returns a
	pointer of type PyTypeObject* , except when the incremented reference
	count is needed."""
		dll.PyObject_Size.restype = c_ssize_t
		dll.PyObject_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyObject_Size.__doc__ = """Return the length of object o .  If the object o provides either the sequence
	and mapping protocols, the sequence length is returned.  On error, -1 is
	returned.  This is the equivalent to the Python expression len(o) . Changed in version 2.5: These functions returned an c_int type. This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyObject_Length.restype = c_ssize_t
		dll.PyObject_Length.argtypes = [ POINTER(PyObject) ]
		dll._PyObject_LengthHint.restype = c_ssize_t
		dll._PyObject_LengthHint.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PyObject_GetItem.restype = POINTER(PyObject)
		dll.PyObject_GetItem.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_GetItem.__doc__ = """Return value: New reference. Return element of o corresponding to the object key or NULL on failure.
	This is the equivalent of the Python expression o[key] ."""
		dll.PyObject_SetItem.restype = c_int
		dll.PyObject_SetItem.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_SetItem.__doc__ = """Map the object key to the value v .  Returns -1 on failure.  This is the
	equivalent of the Python statement o[key] = v ."""
		dll.PyObject_DelItemString.restype = c_int
		dll.PyObject_DelItemString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyObject_DelItem.restype = c_int
		dll.PyObject_DelItem.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_DelItem.__doc__ = """Delete the mapping for key from o .  Returns -1 on failure. This is the
	equivalent of the Python statement del o[key] ."""
		dll.PyObject_AsCharBuffer.restype = c_int
		dll.PyObject_AsCharBuffer.argtypes = [ POINTER(PyObject), POINTER(c_char_p), POINTER(c_ssize_t) ]
		dll.PyObject_AsCharBuffer.__doc__ = """Returns a pointer to a read-only memory location usable as character-based
	input.  The obj argument must support the single-segment character buffer
	interface.  On success, returns 0 , sets buffer to the memory location
	and buffer_len to the buffer length.  Returns -1 and sets a TypeError on error. New in version 1.6. Changed in version 2.5: This function used an c_int * type for buffer_len . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PyObject_CheckReadBuffer.restype = c_int
		dll.PyObject_CheckReadBuffer.argtypes = [ POINTER(PyObject) ]
		dll.PyObject_CheckReadBuffer.__doc__ = """Returns 1 if o supports the single-segment readable buffer interface.
	Otherwise returns 0 . New in version 2.2."""
		dll.PyObject_AsReadBuffer.restype = c_int
		dll.PyObject_AsReadBuffer.argtypes = [ POINTER(PyObject), POINTER(c_void_p), POINTER(c_ssize_t) ]
		dll.PyObject_AsReadBuffer.__doc__ = """Returns a pointer to a read-only memory location containing arbitrary data.
	The obj argument must support the single-segment readable buffer
	interface.  On success, returns 0 , sets buffer to the memory location
	and buffer_len to the buffer length.  Returns -1 and sets a TypeError on error. New in version 1.6. Changed in version 2.5: This function used an c_int * type for buffer_len . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PyObject_AsWriteBuffer.restype = c_int
		dll.PyObject_AsWriteBuffer.argtypes = [ POINTER(PyObject), POINTER(c_void_p), POINTER(c_ssize_t) ]
		dll.PyObject_AsWriteBuffer.__doc__ = """Returns a pointer to a writeable memory location.  The obj argument must
	support the single-segment, character buffer interface.  On success,
	returns 0 , sets buffer to the memory location and buffer_len to the
	buffer length.  Returns -1 and sets a TypeError on error. New in version 1.6. Changed in version 2.5: This function used an c_int * type for buffer_len . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PyObject_GetBuffer.restype = c_int
		dll.PyObject_GetBuffer.argtypes = [ POINTER(PyObject), POINTER(py_object), c_int ]
		dll.PyObject_GetBuffer.__doc__ = """Export obj into a Py_buffer , view .  These arguments must
	never be NULL .  The flags argument is a bit field indicating what
	kind of buffer the caller is prepared to deal with and therefore what
	kind of buffer the exporter is allowed to return.  The buffer interface
	allows for complicated memory sharing possibilities, but some caller may
	not be able to handle all the complexity but may want to see if the
	exporter will let them take a simpler view to its memory. Some exporters may not be able to share memory in every possible way and
	may need to raise errors to signal to some consumers that something is
	just not possible. These errors should be a BufferError unless
	there is another error that is actually causing the problem. The
	exporter can use flags information to simplify how much of the Py_buffer structure is filled in with non-default values and/or
	raise an error if the object can't support a simpler view of its memory. 0 is returned on success and -1 on error. The following table gives possible values to the flags arguments. Flag Description PyBUF_SIMPLE This is the default flag state.  The returned
	buffer may or may not have writable memory.  The
	format of the data will be assumed to be unsigned
	bytes.  This is a "stand-alone" flag constant. It
	never needs to be '|'d to the others. The exporter
	will raise an error if it cannot provide such a
	contiguous buffer of bytes. PyBUF_WRITABLE The returned buffer must be writable.  If it is
	not writable, then raise an error. PyBUF_STRIDES This implies PyBUF_ND . The returned
	buffer must provide strides information (i.e. the
	strides cannot be NULL). This would be used when
	the consumer can handle strided, discontiguous
	arrays.  Handling strides automatically assumes
	you can handle shape.  The exporter can raise an
	error if a strided representation of the data is
	not possible (i.e. without the suboffsets). PyBUF_ND The returned buffer must provide shape
	information. The memory will be assumed C-style
	contiguous (last dimension varies the
	fastest). The exporter may raise an error if it
	cannot provide this kind of contiguous buffer. If
	this is not given then shape will be NULL . PyBUF_C_CONTIGUOUS PyBUF_F_CONTIGUOUS PyBUF_ANY_CONTIGUOUS These flags indicate that the contiguity returned
	buffer must be respectively, C-contiguous (last
	dimension varies the fastest), Fortran contiguous
	(first dimension varies the fastest) or either
	one.  All of these flags imply PyBUF_STRIDES and guarantee that the
	strides buffer info structure will be filled in
	correctly. PyBUF_INDIRECT This flag indicates the returned buffer must have
	suboffsets information (which can be NULL if no
	suboffsets are needed).  This can be used when
	the consumer can handle indirect array
	referencing implied by these suboffsets. This
	implies PyBUF_STRIDES . PyBUF_FORMAT The returned buffer must have true format
	information if this flag is provided. This would
	be used when the consumer is going to be checking
	for what 'kind' of data is actually stored. An
	exporter should always be able to provide this
	information if requested. If format is not
	explicitly requested then the format must be
	returned as NULL (which means 'B' , or
	unsigned bytes) PyBUF_STRIDED This is equivalent to (PyBUF_STRIDES | PyBUF_WRITABLE) . PyBUF_STRIDED_RO This is equivalent to (PyBUF_STRIDES) . PyBUF_RECORDS This is equivalent to (PyBUF_STRIDES | PyBUF_FORMAT | PyBUF_WRITABLE) . PyBUF_RECORDS_RO This is equivalent to (PyBUF_STRIDES | PyBUF_FORMAT) . PyBUF_FULL This is equivalent to (PyBUF_INDIRECT | PyBUF_FORMAT | PyBUF_WRITABLE) . PyBUF_FULL_RO This is equivalent to (PyBUF_INDIRECT | PyBUF_FORMAT) . PyBUF_CONTIG This is equivalent to (PyBUF_ND | PyBUF_WRITABLE) . PyBUF_CONTIG_RO This is equivalent to (PyBUF_ND) ."""
		dll.PyBuffer_GetPointer.restype = c_void_p
		dll.PyBuffer_GetPointer.argtypes = [ POINTER(py_object), POINTER(c_ssize_t) ]
		dll.PyBuffer_SizeFromFormat.restype = c_int
		dll.PyBuffer_SizeFromFormat.argtypes = [ c_char_p ]
		dll.PyBuffer_SizeFromFormat.__doc__ = """Return the implied itemsize from the struct-stype format ."""
		dll.PyBuffer_ToContiguous.restype = c_int
		dll.PyBuffer_ToContiguous.argtypes = [ c_void_p, POINTER(py_object), c_ssize_t, c_char ]
		dll.PyBuffer_FromContiguous.restype = c_int
		dll.PyBuffer_FromContiguous.argtypes = [ POINTER(py_object), c_void_p, c_ssize_t, c_char ]
		dll.PyObject_CopyData.restype = c_int
		dll.PyObject_CopyData.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyBuffer_IsContiguous.restype = c_int
		dll.PyBuffer_IsContiguous.argtypes = [ POINTER(py_object), c_char ]
		dll.PyBuffer_IsContiguous.__doc__ = """Return 1 if the memory defined by the view is C-style ( fortran is 'C' ) or Fortran-style ( fortran is 'F' ) contiguous or either one
	( fortran is 'A' ).  Return 0 otherwise."""
		dll.PyBuffer_FillContiguousStrides.restype = None
		dll.PyBuffer_FillContiguousStrides.argtypes = [ c_int, POINTER(c_ssize_t), POINTER(c_ssize_t), c_int, c_char ]
		dll.PyBuffer_FillContiguousStrides.__doc__ = """Fill the strides array with byte-strides of a contiguous (C-style if fortran is 'C' or Fortran-style if fortran is 'F' ) array of the
	given shape with the given number of bytes per element."""
		dll.PyBuffer_FillInfo.restype = c_int
		dll.PyBuffer_FillInfo.argtypes = [ POINTER(py_object), POINTER(PyObject), c_void_p, c_ssize_t, c_int, c_int ]
		dll.PyBuffer_FillInfo.__doc__ = """Fill in a buffer-info structure, view , correctly for an exporter that can
	only share a contiguous chunk of memory of "unsigned bytes" of the given
	length.  Return 0 on success and -1 (with raising an error) on error."""
		dll.PyBuffer_Release.restype = None
		dll.PyBuffer_Release.argtypes = [ POINTER(py_object) ]
		dll.PyBuffer_Release.__doc__ = """Release the buffer view .  This should be called when the buffer
	is no longer being used as it may free memory from it."""
		dll.PyObject_Format.restype = POINTER(PyObject)
		dll.PyObject_Format.argtypes = [ POINTER(py_object), POINTER(PyObject) ]
		dll.PyObject_GetIter.restype = POINTER(PyObject)
		dll.PyObject_GetIter.argtypes = [ POINTER(PyObject) ]
		dll.PyObject_GetIter.__doc__ = """Return value: New reference. This is equivalent to the Python expression iter(o) . It returns a new
	iterator for the object argument, or the object  itself if the object is already
	an iterator.  Raises TypeError and returns NULL if the object cannot be
	iterated."""
		dll.PyIter_Next.restype = POINTER(PyObject)
		dll.PyIter_Next.argtypes = [ POINTER(PyObject) ]
		dll.PyIter_Next.__doc__ = """Return value: New reference. Return the next value from the iteration o .  If the object is an iterator,
	this retrieves the next value from the iteration, and returns NULL with no
	exception set if there are no remaining items.  If the object is not an
	iterator, TypeError is raised, or if there is an error in retrieving the
	item, returns NULL and passes along the exception."""
		dll.PyNumber_Check.restype = c_int
		dll.PyNumber_Check.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Check.__doc__ = """Returns 1 if the object o provides numeric protocols, and false otherwise.
	This function always succeeds."""
		dll.PyNumber_Add.restype = POINTER(PyObject)
		dll.PyNumber_Add.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Add.__doc__ = """Return value: New reference. Returns the result of adding o1 and o2 , or NULL on failure.  This is the
	equivalent of the Python expression o1 + o2 ."""
		dll.PyNumber_Subtract.restype = POINTER(PyObject)
		dll.PyNumber_Subtract.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Subtract.__doc__ = """Return value: New reference. Returns the result of subtracting o2 from o1 , or NULL on failure.  This is
	the equivalent of the Python expression o1 - o2 ."""
		dll.PyNumber_Multiply.restype = POINTER(PyObject)
		dll.PyNumber_Multiply.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Multiply.__doc__ = """Return value: New reference. Returns the result of multiplying o1 and o2 , or NULL on failure.  This is
	the equivalent of the Python expression o1 * o2 ."""
		dll.PyNumber_Divide.restype = POINTER(PyObject)
		dll.PyNumber_Divide.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Divide.__doc__ = """Return value: New reference. Returns the result of dividing o1 by o2 , or NULL on failure.  This is the
	equivalent of the Python expression o1 / o2 ."""
		dll.PyNumber_FloorDivide.restype = POINTER(PyObject)
		dll.PyNumber_FloorDivide.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_FloorDivide.__doc__ = """Return value: New reference. Return the floor of o1 divided by o2 , or NULL on failure.  This is
	equivalent to the "classic" division of integers. New in version 2.2."""
		dll.PyNumber_TrueDivide.restype = POINTER(PyObject)
		dll.PyNumber_TrueDivide.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_TrueDivide.__doc__ = """Return value: New reference. Return a reasonable approximation for the mathematical value of o1 divided by o2 , or NULL on failure.  The return value is "approximate" because binary
	floating point numbers are approximate; it is not possible to represent all real
	numbers in base two.  This function can return a floating point value when
	passed two integers. New in version 2.2."""
		dll.PyNumber_Remainder.restype = POINTER(PyObject)
		dll.PyNumber_Remainder.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Remainder.__doc__ = """Return value: New reference. Returns the remainder of dividing o1 by o2 , or NULL on failure.  This is
	the equivalent of the Python expression o1 % o2 ."""
		dll.PyNumber_Divmod.restype = POINTER(PyObject)
		dll.PyNumber_Divmod.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Divmod.__doc__ = """Return value: New reference. See the built-in function divmod() . Returns NULL on failure.  This is
	the equivalent of the Python expression divmod(o1, o2) ."""
		dll.PyNumber_Power.restype = POINTER(PyObject)
		dll.PyNumber_Power.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Power.__doc__ = """Return value: New reference. See the built-in function pow() . Returns NULL on failure.  This is the
	equivalent of the Python expression pow(o1, o2, o3) , where o3 is optional.
	If o3 is to be ignored, pass Py_None in its place (passing NULL for o3 would cause an illegal memory access)."""
		dll.PyNumber_Negative.restype = POINTER(PyObject)
		dll.PyNumber_Negative.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Negative.__doc__ = """Return value: New reference. Returns the negation of o on success, or NULL on failure. This is the
	equivalent of the Python expression -o ."""
		dll.PyNumber_Positive.restype = POINTER(PyObject)
		dll.PyNumber_Positive.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Positive.__doc__ = """Return value: New reference. Returns o on success, or NULL on failure.  This is the equivalent of the
	Python expression +o ."""
		dll.PyNumber_Absolute.restype = POINTER(PyObject)
		dll.PyNumber_Absolute.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Absolute.__doc__ = """Return value: New reference. Returns the absolute value of o , or NULL on failure.  This is the equivalent
	of the Python expression abs(o) ."""
		dll.PyNumber_Invert.restype = POINTER(PyObject)
		dll.PyNumber_Invert.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Invert.__doc__ = """Return value: New reference. Returns the bitwise negation of o on success, or NULL on failure.  This is
	the equivalent of the Python expression ~o ."""
		dll.PyNumber_Lshift.restype = POINTER(PyObject)
		dll.PyNumber_Lshift.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Lshift.__doc__ = """Return value: New reference. Returns the result of left shifting o1 by o2 on success, or NULL on
	failure.  This is the equivalent of the Python expression o1 << o2 ."""
		dll.PyNumber_Rshift.restype = POINTER(PyObject)
		dll.PyNumber_Rshift.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Rshift.__doc__ = """Return value: New reference. Returns the result of right shifting o1 by o2 on success, or NULL on
	failure.  This is the equivalent of the Python expression o1 >> o2 ."""
		dll.PyNumber_And.restype = POINTER(PyObject)
		dll.PyNumber_And.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_And.__doc__ = """Return value: New reference. Returns the "bitwise and" of o1 and o2 on success and NULL on failure.
	This is the equivalent of the Python expression o1 & o2 ."""
		dll.PyNumber_Xor.restype = POINTER(PyObject)
		dll.PyNumber_Xor.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Xor.__doc__ = """Return value: New reference. Returns the "bitwise exclusive or" of o1 by o2 on success, or NULL on
	failure.  This is the equivalent of the Python expression o1 ^ o2 ."""
		dll.PyNumber_Or.restype = POINTER(PyObject)
		dll.PyNumber_Or.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_Or.__doc__ = """Return value: New reference. Returns the "bitwise or" of o1 and o2 on success, or NULL on failure.
	This is the equivalent of the Python expression o1 | o2 ."""
		dll.PyNumber_Index.restype = POINTER(PyObject)
		dll.PyNumber_Index.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Index.__doc__ = """Returns the o converted to a Python c_int or long on success or NULL with a TypeError exception raised on failure. New in version 2.5."""
		dll.PyNumber_AsSsize_t.restype = c_ssize_t
		dll.PyNumber_AsSsize_t.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_AsSsize_t.__doc__ = """Returns o converted to a Py_ssize_t value if o can be interpreted as an
	integer. If o can be converted to a Python c_int or long but the attempt to
	convert to a Py_ssize_t value would raise an OverflowError , then the exc argument is the type of exception that will be raised (usually IndexError or OverflowError ).  If exc is NULL , then the
	exception is cleared and the value is clipped to PY_SSIZE_T_MIN for a negative
	integer or PY_SSIZE_T_MAX for a positive integer. New in version 2.5."""
		dll._PyNumber_ConvertIntegralToInt.restype = POINTER(PyObject)
		dll._PyNumber_ConvertIntegralToInt.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyNumber_Int.restype = POINTER(PyObject)
		dll.PyNumber_Int.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Int.__doc__ = """Return value: New reference. Returns the o converted to an integer object on success, or NULL on failure.
	If the argument is outside the integer range a long object will be returned
	instead. This is the equivalent of the Python expression c_int(o) ."""
		dll.PyNumber_Long.restype = POINTER(PyObject)
		dll.PyNumber_Long.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Long.__doc__ = """Return value: New reference. Returns the o converted to a long integer object on success, or NULL on
	failure.  This is the equivalent of the Python expression long(o) ."""
		dll.PyNumber_Float.restype = POINTER(PyObject)
		dll.PyNumber_Float.argtypes = [ POINTER(PyObject) ]
		dll.PyNumber_Float.__doc__ = """Return value: New reference. Returns the o converted to a float object on success, or NULL on failure.
	This is the equivalent of the Python expression float(o) ."""
		dll.PyNumber_InPlaceAdd.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceAdd.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceAdd.__doc__ = """Return value: New reference. Returns the result of adding o1 and o2 , or NULL on failure.  The operation
	is done in-place when o1 supports it.  This is the equivalent of the Python
	statement o1 += o2 ."""
		dll.PyNumber_InPlaceSubtract.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceSubtract.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceSubtract.__doc__ = """Return value: New reference. Returns the result of subtracting o2 from o1 , or NULL on failure.  The
	operation is done in-place when o1 supports it.  This is the equivalent of
	the Python statement o1 -= o2 ."""
		dll.PyNumber_InPlaceMultiply.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceMultiply.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceMultiply.__doc__ = """Return value: New reference. Returns the result of multiplying o1 and o2 , or NULL on failure.  The
	operation is done in-place when o1 supports it.  This is the equivalent of
	the Python statement o1 *= o2 ."""
		dll.PyNumber_InPlaceDivide.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceDivide.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceDivide.__doc__ = """Return value: New reference. Returns the result of dividing o1 by o2 , or NULL on failure.  The
	operation is done in-place when o1 supports it. This is the equivalent of
	the Python statement o1 /= o2 ."""
		dll.PyNumber_InPlaceFloorDivide.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceFloorDivide.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceFloorDivide.__doc__ = """Return value: New reference. Returns the mathematical floor of dividing o1 by o2 , or NULL on failure.
	The operation is done in-place when o1 supports it.  This is the equivalent
	of the Python statement o1 //= o2 . New in version 2.2."""
		dll.PyNumber_InPlaceTrueDivide.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceTrueDivide.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceTrueDivide.__doc__ = """Return value: New reference. Return a reasonable approximation for the mathematical value of o1 divided by o2 , or NULL on failure.  The return value is "approximate" because binary
	floating point numbers are approximate; it is not possible to represent all real
	numbers in base two.  This function can return a floating point value when
	passed two integers.  The operation is done in-place when o1 supports it. New in version 2.2."""
		dll.PyNumber_InPlaceRemainder.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceRemainder.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceRemainder.__doc__ = """Return value: New reference. Returns the remainder of dividing o1 by o2 , or NULL on failure.  The
	operation is done in-place when o1 supports it.  This is the equivalent of
	the Python statement o1 %= o2 ."""
		dll.PyNumber_InPlacePower.restype = POINTER(PyObject)
		dll.PyNumber_InPlacePower.argtypes = [ POINTER(PyObject), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlacePower.__doc__ = """Return value: New reference. See the built-in function pow() . Returns NULL on failure.  The operation
	is done in-place when o1 supports it.  This is the equivalent of the Python
	statement o1 **= o2 when o3 is Py_None , or an in-place variant of pow(o1, o2, o3) otherwise. If o3 is to be ignored, pass Py_None in its place (passing NULL for o3 would cause an illegal memory access)."""
		dll.PyNumber_InPlaceLshift.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceLshift.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceLshift.__doc__ = """Return value: New reference. Returns the result of left shifting o1 by o2 on success, or NULL on
	failure.  The operation is done in-place when o1 supports it.  This is the
	equivalent of the Python statement o1 <<= o2 ."""
		dll.PyNumber_InPlaceRshift.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceRshift.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceRshift.__doc__ = """Return value: New reference. Returns the result of right shifting o1 by o2 on success, or NULL on
	failure.  The operation is done in-place when o1 supports it.  This is the
	equivalent of the Python statement o1 >>= o2 ."""
		dll.PyNumber_InPlaceAnd.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceAnd.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceAnd.__doc__ = """Return value: New reference. Returns the "bitwise and" of o1 and o2 on success and NULL on failure. The
	operation is done in-place when o1 supports it.  This is the equivalent of
	the Python statement o1 &= o2 ."""
		dll.PyNumber_InPlaceXor.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceXor.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceXor.__doc__ = """Return value: New reference. Returns the "bitwise exclusive or" of o1 by o2 on success, or NULL on
	failure.  The operation is done in-place when o1 supports it.  This is the
	equivalent of the Python statement o1 ^= o2 ."""
		dll.PyNumber_InPlaceOr.restype = POINTER(PyObject)
		dll.PyNumber_InPlaceOr.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNumber_InPlaceOr.__doc__ = """Return value: New reference. Returns the "bitwise or" of o1 and o2 on success, or NULL on failure.  The
	operation is done in-place when o1 supports it.  This is the equivalent of
	the Python statement o1 |= o2 ."""
		dll.PyNumber_ToBase.restype = POINTER(PyObject)
		dll.PyNumber_ToBase.argtypes = [ POINTER(PyObject), c_int ]
		dll.PyNumber_ToBase.__doc__ = """Returns the integer n converted to base as a string with a base
	marker of '0b' , '0o' , or '0x' if applicable.  When base is not 2, 8, 10, or 16, the format is 'x#num' where x is the
	base. If n is not an c_int object, it is converted with PyNumber_Index() first. New in version 2.6."""
		dll.PySequence_Check.restype = c_int
		dll.PySequence_Check.argtypes = [ POINTER(PyObject) ]
		dll.PySequence_Check.__doc__ = """Return 1 if the object provides sequence protocol, and 0 otherwise.
	This function always succeeds."""
		dll.PySequence_Size.restype = c_ssize_t
		dll.PySequence_Size.argtypes = [ POINTER(PyObject) ]
		dll.PySequence_Length.restype = c_ssize_t
		dll.PySequence_Length.argtypes = [ POINTER(PyObject) ]
		dll.PySequence_Length.__doc__ = """Returns the number of objects in sequence o on success, and -1 on failure.
	For objects that do not provide sequence protocol, this is equivalent to the
	Python expression len(o) . Changed in version 2.5: These functions returned an c_int type. This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_Concat.restype = POINTER(PyObject)
		dll.PySequence_Concat.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySequence_Concat.__doc__ = """Return value: New reference. Return the concatenation of o1 and o2 on success, and NULL on failure.
	This is the equivalent of the Python expression o1 + o2 ."""
		dll.PySequence_Repeat.restype = POINTER(PyObject)
		dll.PySequence_Repeat.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PySequence_Repeat.__doc__ = """Return value: New reference. Return the result of repeating sequence object o count times, or NULL on
	failure.  This is the equivalent of the Python expression o * count . Changed in version 2.5: This function used an c_int type for count . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_GetItem.restype = POINTER(PyObject)
		dll.PySequence_GetItem.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PySequence_GetItem.__doc__ = """Return value: New reference. Return the i th element of o , or NULL on failure. This is the equivalent of
	the Python expression o[i] . Changed in version 2.5: This function used an c_int type for i . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_GetSlice.restype = POINTER(PyObject)
		dll.PySequence_GetSlice.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PySequence_GetSlice.__doc__ = """Return value: New reference. Return the slice of sequence object o between i1 and i2 , or NULL on
	failure. This is the equivalent of the Python expression o[i1:i2] . Changed in version 2.5: This function used an c_int type for i1 and i2 . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_SetItem.restype = c_int
		dll.PySequence_SetItem.argtypes = [ POINTER(PyObject), c_ssize_t, POINTER(PyObject) ]
		dll.PySequence_SetItem.__doc__ = """Assign object v to the i th element of o .  Returns -1 on failure.  This
	is the equivalent of the Python statement o[i] = v .  This function does
	not steal a reference to v . Changed in version 2.5: This function used an c_int type for i . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_DelItem.restype = c_int
		dll.PySequence_DelItem.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PySequence_DelItem.__doc__ = """Delete the i th element of object o .  Returns -1 on failure.  This is the
	equivalent of the Python statement del o[i] . Changed in version 2.5: This function used an c_int type for i . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_SetSlice.restype = c_int
		dll.PySequence_SetSlice.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t, POINTER(PyObject) ]
		dll.PySequence_SetSlice.__doc__ = """Assign the sequence object v to the slice in sequence object o from i1 to i2 .  This is the equivalent of the Python statement o[i1:i2] = v . Changed in version 2.5: This function used an c_int type for i1 and i2 . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_DelSlice.restype = c_int
		dll.PySequence_DelSlice.argtypes = [ POINTER(PyObject), c_ssize_t, c_ssize_t ]
		dll.PySequence_DelSlice.__doc__ = """Delete the slice in sequence object o from i1 to i2 .  Returns -1 on
	failure.  This is the equivalent of the Python statement del o[i1:i2] . Changed in version 2.5: This function used an c_int type for i1 and i2 . This might
	require changes in your code for properly supporting 64-bit systems."""
		dll.PySequence_Tuple.restype = POINTER(PyObject)
		dll.PySequence_Tuple.argtypes = [ POINTER(PyObject) ]
		dll.PySequence_Tuple.__doc__ = """Return value: New reference. Return a tuple object with the same contents as the arbitrary sequence o or NULL on failure.  If o is a tuple, a new reference will be returned,
	otherwise a tuple will be constructed with the appropriate contents.  This is
	equivalent to the Python expression tuple(o) ."""
		dll.PySequence_List.restype = POINTER(PyObject)
		dll.PySequence_List.argtypes = [ POINTER(PyObject) ]
		dll.PySequence_List.__doc__ = """Return value: New reference. Return a list object with the same contents as the arbitrary sequence o .  The
	returned list is guaranteed to be new."""
		dll.PySequence_Fast.restype = POINTER(PyObject)
		dll.PySequence_Fast.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PySequence_Fast.__doc__ = """Return value: New reference. Returns the sequence o as a tuple, unless it is already a tuple or list, in
	which case o is returned.  Use PySequence_Fast_GET_ITEM() to access the
	members of the result.  Returns NULL on failure.  If the object is not a
	sequence, raises TypeError with m as the message text."""
		dll.PySequence_Count.restype = c_ssize_t
		dll.PySequence_Count.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySequence_Count.__doc__ = """Return the number of occurrences of value in o , that is, return the number
	of keys for which o[key] == value .  On failure, return -1 .  This is
	equivalent to the Python expression o.count(value) . Changed in version 2.5: This function returned an c_int type. This might require changes
	in your code for properly supporting 64-bit systems."""
		dll.PySequence_Contains.restype = c_int
		dll.PySequence_Contains.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySequence_Contains.__doc__ = """Determine if o contains value .  If an item in o is equal to value ,
	return 1 , otherwise return 0 . On error, return -1 .  This is
	equivalent to the Python expression value in o ."""
		dll._PySequence_IterSearch.restype = c_ssize_t
		dll._PySequence_IterSearch.argtypes = [ POINTER(PyObject), POINTER(PyObject), c_int ]
		dll.PySequence_In.restype = c_int
		dll.PySequence_In.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySequence_Index.restype = c_ssize_t
		dll.PySequence_Index.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySequence_Index.__doc__ = """Return the first index i for which o[i] == value .  On error, return -1 .    This is equivalent to the Python expression o.index(value) . Changed in version 2.5: This function returned an c_int type. This might require changes
	in your code for properly supporting 64-bit systems."""
		dll.PySequence_InPlaceConcat.restype = POINTER(PyObject)
		dll.PySequence_InPlaceConcat.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PySequence_InPlaceConcat.__doc__ = """Return value: New reference. Return the concatenation of o1 and o2 on success, and NULL on failure.
	The operation is done in-place when o1 supports it.  This is the equivalent
	of the Python expression o1 += o2 ."""
		dll.PySequence_InPlaceRepeat.restype = POINTER(PyObject)
		dll.PySequence_InPlaceRepeat.argtypes = [ POINTER(PyObject), c_ssize_t ]
		dll.PySequence_InPlaceRepeat.__doc__ = """Return value: New reference. Return the result of repeating sequence object o count times, or NULL on
	failure.  The operation is done in-place when o supports it.  This is the
	equivalent of the Python expression o *= count . Changed in version 2.5: This function used an c_int type for count . This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyMapping_Check.restype = c_int
		dll.PyMapping_Check.argtypes = [ POINTER(PyObject) ]
		dll.PyMapping_Check.__doc__ = """Return 1 if the object provides mapping protocol, and 0 otherwise.  This
	function always succeeds."""
		dll.PyMapping_Size.restype = c_ssize_t
		dll.PyMapping_Size.argtypes = [ POINTER(PyObject) ]
		dll.PyMapping_Length.restype = c_ssize_t
		dll.PyMapping_Length.argtypes = [ POINTER(PyObject) ]
		dll.PyMapping_Length.__doc__ = """Returns the number of keys in object o on success, and -1 on failure.  For
	objects that do not provide mapping protocol, this is equivalent to the Python
	expression len(o) . Changed in version 2.5: These functions returned an c_int type. This might require
	changes in your code for properly supporting 64-bit systems."""
		dll.PyMapping_HasKeyString.restype = c_int
		dll.PyMapping_HasKeyString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyMapping_HasKeyString.__doc__ = """On success, return 1 if the mapping object has the key key and 0 otherwise.  This is equivalent to o[key] , returning True on success
	and False on an exception.  This function always succeeds."""
		dll.PyMapping_HasKey.restype = c_int
		dll.PyMapping_HasKey.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyMapping_HasKey.__doc__ = """Return 1 if the mapping object has the key key and 0 otherwise.
	This is equivalent to o[key] , returning True on success and False on an exception.  This function always succeeds."""
		dll.PyMapping_GetItemString.restype = POINTER(PyObject)
		dll.PyMapping_GetItemString.argtypes = [ POINTER(PyObject), c_char_p ]
		dll.PyMapping_GetItemString.__doc__ = """Return value: New reference. Return element of o corresponding to the object key or NULL on failure.
	This is the equivalent of the Python expression o[key] ."""
		dll.PyMapping_SetItemString.restype = c_int
		dll.PyMapping_SetItemString.argtypes = [ POINTER(PyObject), c_char_p, POINTER(PyObject) ]
		dll.PyMapping_SetItemString.__doc__ = """Map the object key to the value v in object o . Returns -1 on failure.
	This is the equivalent of the Python statement o[key] = v ."""
		dll.PyObject_IsInstance.restype = c_int
		dll.PyObject_IsInstance.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_IsInstance.__doc__ = """Returns 1 if inst is an instance of the class cls or a subclass of cls , or 0 if not.  On error, returns -1 and sets an exception.  If cls is a type object rather than a class object, PyObject_IsInstance() returns 1 if inst is of type cls .  If cls is a tuple, the check will
	be done against every entry in cls . The result will be 1 when at least one
	of the checks returns 1 , otherwise it will be 0 . If inst is not a
	class instance and cls is neither a type object, nor a class object, nor a
	tuple, inst must have a __class__ attribute - the class relationship
	of the value of that attribute with cls will be used to determine the result
	of this function. New in version 2.1. Changed in version 2.2: Support for a tuple as the second argument added."""
		dll.PyObject_IsSubclass.restype = c_int
		dll.PyObject_IsSubclass.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyObject_IsSubclass.__doc__ = """Returns 1 if the class derived is identical to or derived from the class cls , otherwise returns 0 .  In case of an error, returns -1 . If cls is a tuple, the check will be done against every entry in cls . The result will
	be 1 when at least one of the checks returns 1 , otherwise it will be 0 . If either derived or cls is not an actual class object (or tuple),
	this function uses the generic algorithm described above. New in version 2.1. Changed in version 2.3: Older versions of Python did not support a tuple as the second argument."""
		dll._PyObject_RealIsInstance.restype = c_int
		dll._PyObject_RealIsInstance.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll._PyObject_RealIsSubclass.restype = c_int
		dll._PyObject_RealIsSubclass.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll._Py_add_one_to_index_F.restype = None
		dll._Py_add_one_to_index_F.argtypes = [ c_int, POINTER(c_ssize_t), POINTER(c_ssize_t) ]
		dll._Py_add_one_to_index_C.restype = None
		dll._Py_add_one_to_index_C.argtypes = [ c_int, POINTER(c_ssize_t), POINTER(c_ssize_t) ]
		dll.PyCode_New.restype = POINTER(py_object)
		dll.PyCode_New.argtypes = [ c_int, c_int, c_int, c_int, POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), POINTER(PyObject), c_int, POINTER(PyObject) ]
		dll.PyCode_New.__doc__ = """Return a new code object.  If you need a dummy code object to
	create a frame, use PyCode_NewEmpty() instead.  Calling PyCode_New() directly can bind you to a precise Python
	version since the definition of the bytecode changes often."""
		dll.PyCode_NewEmpty.restype = POINTER(py_object)
		dll.PyCode_NewEmpty.argtypes = [ c_char_p, c_char_p, c_int ]
		dll.PyCode_NewEmpty.__doc__ = """Return a new empty code object with the specified filename,
	function name, and first line number.  It is illegal to exec or eval() the resulting code object."""
		dll.PyCode_Addr2Line.restype = c_int
		dll.PyCode_Addr2Line.argtypes = [ POINTER(py_object), c_int ]
		dll._PyCode_CheckLineNumber.restype = c_int
		dll._PyCode_CheckLineNumber.argtypes = [ POINTER(py_object), c_int, POINTER(py_object) ]
		dll.PyCode_Optimize.restype = POINTER(PyObject)
		dll.PyCode_Optimize.argtypes = [ POINTER(PyObject), POINTER(py_object), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyNode_Compile.restype = POINTER(py_object)
		dll.PyNode_Compile.argtypes = [ c_void_p, c_char_p ] # POINTER(struct _node)
		dll.PyAST_Compile.restype = POINTER(py_object)
		dll.PyAST_Compile.argtypes = [ c_void_p, c_char_p, POINTER(py_object), POINTER(py_object) ] # POINTER(struct _mod)
		dll.PyFuture_FromAST.restype = POINTER(py_object)
		dll.PyFuture_FromAST.argtypes = [ c_void_p, c_char_p ] # POINTER(struct _mod)
		dll.PyEval_EvalCode.restype = POINTER(PyObject)
		dll.PyEval_EvalCode.argtypes = [ POINTER(py_object), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyEval_EvalCode.__doc__ = """Return value: New reference. This is a simplified interface to PyEval_EvalCodeEx() , with just
	the code object, and the dictionaries of global and local variables.
	The other arguments are set to NULL ."""
		dll.PyEval_EvalCodeEx.restype = POINTER(PyObject)
		dll.PyEval_EvalCodeEx.argtypes = [ POINTER(py_object), POINTER(PyObject), POINTER(PyObject), POINTER(POINTER(PyObject)), c_int, POINTER(POINTER(PyObject)), c_int, POINTER(POINTER(PyObject)), c_int, POINTER(PyObject) ]
		dll.PyEval_EvalCodeEx.__doc__ = """Evaluate a precompiled code object, given a particular environment for its
	evaluation.  This environment consists of dictionaries of global and local
	variables, arrays of arguments, keywords and defaults, and a closure tuple of
	cells."""
		dll._PyEval_CallTracing.restype = POINTER(PyObject)
		dll._PyEval_CallTracing.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.PyOS_ascii_strtod.restype = c_double
		dll.PyOS_ascii_strtod.argtypes = [ c_char_p, POINTER(c_char_p) ]
		dll.PyOS_ascii_strtod.__doc__ = """Convert a string to a double . This function behaves like the Standard C
	function strtod() does in the C locale. It does this without changing the
	current locale, since that would not be thread-safe. PyOS_ascii_strtod() should typically be used for reading configuration
	files or other non-user input that should be locale independent. See the Unix man page strtod(2) for details. New in version 2.4. Deprecated since version 2.7: Use PyOS_string_to_double() instead."""
		dll.PyOS_ascii_atof.restype = c_double
		dll.PyOS_ascii_atof.argtypes = [ c_char_p ]
		dll.PyOS_ascii_atof.__doc__ = """Convert a string to a double in a locale-independent way. See the Unix man page atof(2) for details. New in version 2.4. Deprecated since version 3.1: Use PyOS_string_to_double() instead."""
		dll.PyOS_ascii_formatd.restype = c_char_p
		dll.PyOS_ascii_formatd.argtypes = [ c_char_p, c_size_t, c_char_p, c_double ]
		dll.PyOS_ascii_formatd.__doc__ = """Convert a double to a string using the '.' as the decimal
	separator. format is a printf() -style format string specifying the
	number format. Allowed conversion characters are 'e' , 'E' , 'f' , 'F' , 'g' and 'G' . The return value is a pointer to buffer with the converted string or NULL if
	the conversion failed. New in version 2.4. Deprecated since version 2.7: This function is removed in Python 2.7 and 3.1.  Use PyOS_double_to_string() instead."""
		dll.PyOS_string_to_double.restype = c_double
		dll.PyOS_string_to_double.argtypes = [ c_char_p, POINTER(c_char_p), POINTER(PyObject) ]
		dll.PyOS_string_to_double.__doc__ = """Convert a string s to a double , raising a Python
	exception on failure.  The set of accepted strings corresponds to
	the set of strings accepted by Python's float() constructor,
	except that s must not have leading or trailing whitespace.
	The conversion is independent of the current locale. If endptr is NULL , convert the whole string.  Raise
	ValueError and return -1.0 if the string is not a valid
	representation of a floating-point number. If endptr is not NULL , convert as much of the string as
	possible and set *endptr to point to the first unconverted
	character.  If no initial segment of the string is the valid
	representation of a floating-point number, set *endptr to point
	to the beginning of the string, raise ValueError, and return -1.0 . If s represents a value that is too large to store in a float
	(for example, "1e500" is such a string on many platforms) then
	if overflow_exception is NULL return Py_HUGE_VAL (with
	an appropriate sign) and don't set any exception.  Otherwise, overflow_exception must point to a Python exception object;
	raise that exception and return -1.0 .  In both cases, set *endptr to point to the first character after the converted value. If any other error occurs during the conversion (for example an
	out-of-memory error), set the appropriate Python exception and
	return -1.0 . New in version 2.7."""
		dll.PyOS_double_to_string.restype = c_char_p
		dll.PyOS_double_to_string.argtypes = [ c_double, c_char, c_int, c_int, POINTER(c_int) ]
		dll.PyOS_double_to_string.__doc__ = """Convert a double val to a string using supplied format_code , precision , and flags . format_code must be one of 'e' , 'E' , 'f' , 'F' , 'g' , 'G' or 'r' .  For 'r' , the supplied precision must be 0 and is ignored.  The 'r' format code specifies the
	standard repr() format. flags can be zero or more of the values Py_DTSF_SIGN , Py_DTSF_ADD_DOT_0 , or Py_DTSF_ALT , or-ed together: Py_DTSF_SIGN means to always precede the returned string with a sign
	character, even if val is non-negative. Py_DTSF_ADD_DOT_0 means to ensure that the returned string will not look
	like an integer. Py_DTSF_ALT means to apply "alternate" formatting rules.  See the
	documentation for the PyOS_snprintf() '#' specifier for
	details. If ptype is non-NULL, then the value it points to will be set to one of Py_DTST_FINITE , Py_DTST_INFINITE , or Py_DTST_NAN , signifying that val is a finite number, an infinite number, or not a number, respectively. The return value is a pointer to buffer with the converted string or NULL if the conversion failed. The caller is responsible for freeing the
	returned string by calling PyMem_Free() . New in version 2.7."""
		dll._Py_parse_inf_or_nan.restype = c_double
		dll._Py_parse_inf_or_nan.argtypes = [ c_char_p, POINTER(c_char_p) ]
		dll.PyOS_mystrnicmp.restype = c_int
		dll.PyOS_mystrnicmp.argtypes = [ c_char_p, c_char_p, c_ssize_t ]
		dll.PyOS_mystricmp.restype = c_int
		dll.PyOS_mystricmp.argtypes = [ c_char_p, c_char_p ]
		dll._Py_dg_strtod.restype = c_double
		dll._Py_dg_strtod.argtypes = [ c_char_p, POINTER(c_char_p) ]
		dll._Py_dg_dtoa.restype = c_char_p
		dll._Py_dg_dtoa.argtypes = [ c_double, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_char_p) ]
		dll._Py_dg_freedtoa.restype = None
		dll._Py_dg_freedtoa.argtypes = [ c_char_p ]
		dll._Py_Mangle.restype = POINTER(PyObject)
		dll._Py_Mangle.argtypes = [ POINTER(PyObject), POINTER(PyObject) ]
		dll.newbitset.restype = bitset
		dll.newbitset.argtypes = [ c_int ]
		dll.delbitset.restype = None
		dll.delbitset.argtypes = [ bitset ]
		dll.addbit.restype = c_int
		dll.addbit.argtypes = [ bitset, c_int ]
		dll.samebitset.restype = c_int
		dll.samebitset.argtypes = [ bitset, bitset, c_int ]
		dll.mergebitset.restype = None
		dll.mergebitset.argtypes = [ bitset, bitset, c_int ]
		dll.PyFrame_New.restype = POINTER(py_object)
		dll.PyFrame_New.argtypes = [ POINTER(py_object), POINTER(py_object), POINTER(PyObject), POINTER(PyObject) ]
		dll.PyFrame_BlockSetup.restype = None
		dll.PyFrame_BlockSetup.argtypes = [ POINTER(py_object), c_int, c_int, c_int ]
		dll.PyFrame_BlockPop.restype = POINTER(py_object)
		dll.PyFrame_BlockPop.argtypes = [ POINTER(py_object) ]
		dll.PyFrame_ExtendStack.restype = POINTER(POINTER(PyObject))
		dll.PyFrame_ExtendStack.argtypes = [ POINTER(py_object), c_int, c_int ]
		dll.PyFrame_LocalsToFast.restype = None
		dll.PyFrame_LocalsToFast.argtypes = [ POINTER(py_object), c_int ]
		dll.PyFrame_FastToLocals.restype = None
		dll.PyFrame_FastToLocals.argtypes = [ POINTER(py_object) ]
		dll.PyFrame_ClearFreeList.restype = c_int
		dll.PyFrame_ClearFreeList.argtypes = [  ]
		dll.PyFrame_GetLineNumber.restype = c_int
		dll.PyFrame_GetLineNumber.argtypes = [ POINTER(py_object) ]
		dll.PyFrame_GetLineNumber.__doc__ = """Return the line number that frame is currently executing."""
		dll.PyMember_Get.restype = POINTER(PyObject)
		dll.PyMember_Get.argtypes = [ c_char_p, c_void_p, c_char_p ] # POINTER(struct memberlist)
		dll.PyMember_Set.restype = c_int
		dll.PyMember_Set.argtypes = [ c_char_p, c_void_p, c_char_p, POINTER(PyObject) ] # POINTER(struct memberlist)
		dll.PyMember_GetOne.restype = POINTER(PyObject)
		dll.PyMember_GetOne.argtypes = [ c_char_p, c_void_p ] # POINTER(struct PyMemberDef)
		dll.PyMember_SetOne.restype = c_int
		dll.PyMember_SetOne.argtypes = [ c_char_p, c_void_p, POINTER(PyObject) ] # POINTER(struct PyMemberDef)
	except:
		pass
