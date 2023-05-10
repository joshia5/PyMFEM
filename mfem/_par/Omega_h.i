%module(package="mfem._par", directors="0")  Omega_h

%feature("autodoc", "1");

%{
#include "mesh/mesh_headers.hpp"
#include "mesh/Omega_h.hpp"
#include "fem/fem.hpp"
#include "general/array.hpp"

#include <iostream>
#include <sstream>
#include <fstream>
#include <limits>
#include <cmath>
#include <cstring>
#include <ctime>
#include "../common/io_stream.hpp"         
#include "numpy/arrayobject.h"
#include "pyoperator.hpp"
#include "../common/pycoefficient.hpp"

%}

%include "../common/mfem_config.i"

#ifndef MFEM_USE_MPI
   #define MFEM_USE_MPI  YES
#endif

#ifndef MFEM_USE_OMEGAH
   #define MFEM_USE_OMEGAH YES
#endif

#ifdef MFEM_USE_MPI
%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);
#endif

%init %{
import_array();
%}

//%import "cpointers.i"
%include "exception.i"
%import "../common/numpy_int_typemap.i"
%import "pgridfunc.i"
%import "mesh.i"
%import "pmesh.i"

%include "../common/exception.i"

%inline %{
  mfem::ParOmegaMesh *ParMesh2ParOmegaMesh(mfem::ParMesh *pmesh) {
    return dynamic_cast<mfem::ParOmegaMesh*>(pmesh);
  }
%}

#undef MFEM_USE_OMEGAH
#define MFEM_USE_OMEGAH YES

%include "mesh/Omega_h.hpp"



