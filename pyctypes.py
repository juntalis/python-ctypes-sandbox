from _kernel32 import *
import sys

_pythonDLL = None

def _pythondll():
	global _pythonDLL
	if _pythonDLL is None:
		_pythonDLL = sys.dllhandle, GetModuleFileName(sys.dllhandle)
	return _pythonDLL

c_intptr_t = c_int64 if is_x64() else c_int
c_uintptr_t = c_uint64 if is_x64() else c_uint

class PyObject(Structure):
	_fields_ = [("refcnt", c_size_t),
				("typeid", c_void_p)]

class PyInt(PyObject):
	_fields_ = [("val", c_long)]

class PyFloat(PyObject):
	_fields_ = [("val", c_double)]

class PyVarObject(PyObject):
	_fields_ = [("size", c_size_t)]

class PyStr(PyVarObject):
	_fields_ = [("hash", c_long),
				("state", c_int),
				("_val", c_char*0)]

class PyLong(PyVarObject):
	_fields_ = [("_val", c_uint16*0)]

class PyList(PyVarObject):
	_fields_ = [("items", POINTER(POINTER(PyObject))),
				("allocated", c_size_t)]

	#noinspection PyUnresolvedReferences
	def print_field(self):
		print self.size, self.allocated, byref(self.items[0])

def create_var_object(struct, obj):
	inner_type = None
	for name, t in struct._fields_:
		if name == "_val":
			inner_type = t._type_
	if inner_type is not None:
		tmp = PyVarObject.from_address(id(obj))
		size = tmp.size
		class Inner(struct):
			_fields_ = [("val", inner_type*size)]
		Inner.__name__ = struct.__name__
		struct = Inner
	return struct.from_address(id(obj))



