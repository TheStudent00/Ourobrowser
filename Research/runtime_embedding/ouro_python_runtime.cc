#include <Python.h>
#include "ouro_python_runtime.h"

namespace ourobrowser {

void InitializePythonRuntime() {
    if (!Py_IsInitialized()) {
        Py_Initialize();
        PyEval_InitThreads();
        
        PyRun_SimpleString(
            "import sys\n"
            "print('Ourobrowser Python Runtime Initialized natively inside Blink.')\n"
        );
    }
}

PyObject* CreateFrameContext() {
    PyObject* main_module = PyImport_AddModule("__main__");
    PyObject* main_dict = PyModule_GetDict(main_module);
    PyObject* frame_dict = PyDict_Copy(main_dict);
    return frame_dict;
}

} // namespace ourobrowser
