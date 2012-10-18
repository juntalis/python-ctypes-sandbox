from cutil import *
import sys, os

_pythonDLL = None

def _pythondll():
	global _pythonDLL
	if _pythonDLL is None:
		_pythonDLL = sys.dllhandle, GetModuleFileName(sys.dllhandle)
	return _pythonDLL

class PythonDLL(PyDLL):

	def __init__(self, handle = None, name = None, thread = None):
		if handle is None: handle, name = _pythondll()
		elif name is None: name = GetModuleFileName(handle)
		super(PythonDLL, self).__init__(name, handle=handle)
		self._setup_base()

	def _setup_base(self):
		self.__home = None

	def _initialized(self):
		return self.Py_IsInitialized() == 1

	def _home(self):
		if self.__home is None:
			home = self.Py_GetPythonHome()
			self.__home = None if home == NULL else c_char_p(home).value
		return self._home

	def __getattr__(self, name):
		attr = '_' + name
		if hasattr(self, attr):
			attr = getattr(self, attr)
			return attr() if hasattr(attr, '__call__') else attr
		return super(PythonDLL, self).__getattr__(name)

def clone_python_state(current, target):
	path = os.pathsep.join(sys.path)
	program = current.Py_GetProgramName()
	home = current.Py_GetPythonHome()


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


