#ifndef OUROBROWSER_GIL_SCOPE_H
#define OUROBROWSER_GIL_SCOPE_H

#include <Python.h>

namespace ourobrowser {

class PyGILScope {
public:
    PyGILScope() { 
        gstate_ = PyGILState_Ensure(); 
    }
    ~PyGILScope() { 
        PyGILState_Release(gstate_); 
    }
private:
    PyGILState_STATE gstate_;
};

} // namespace ourobrowser

#endif // OUROBROWSER_GIL_SCOPE_H
