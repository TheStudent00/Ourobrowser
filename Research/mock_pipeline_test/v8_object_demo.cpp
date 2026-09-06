#include "v8/include/v8.h"

void CreateV8Object(PyInterpreterState* isolate) {
    PyDictObject* context = isolate->GetCurrentContext();
    PyObject* obj = v8::Object::New(isolate);
    PyObject* key = PyUnicode_FromString("hello");
    PyObject* value = PyUnicode_FromString("world");
    obj->Set(context, key, value).Check();
}