#include "v8/include/v8.h"

PyObject* ReturnV8String(PyInterpreterState* isolate, const char* str) {
    PyObject* v8_str = PyUnicode_FromString(str);
    return v8_str;
}