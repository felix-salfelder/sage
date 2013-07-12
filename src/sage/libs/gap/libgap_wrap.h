//#############################################################################
//      Copyright (C) 2009, William Stein <wstein@gmail.com>
//      Copyright (C) 2012, Volker Braun <vbraun.name@gmail.com>
//      Copyright (C) 2013, Felix Salfelder
//
//  Distributed under the terms of the GNU General Public License (GPL)
//  as published by the Free Software Foundation; either version 2 of
//  the License, or (at your option) any later version.
//                  http://www.gnu.org/licenses/
//#############################################################################

#ifndef LIBGAP_WRAP_HH
#define LIBGAP_WRAP_HH

#ifdef HAVE_LIBGAP
#include <libgap/config.h>
#include <libgap/system.h>
#include <libgap/code.h>
#include <libgap/gap.h>
#include <libgap/objects.h>
#include <libgap/read.h>
#include <libgap/scanner.h>
#include <libgap/gvars.h>
#include <libgap/string.h>
#include <libgap/gasman.h>
#include <libgap/ariths.h>
#include <libgap/calls.h>
#include <libgap/plist.h>
#include <libgap/lists.h>
#include <libgap/listfunc.h>
#include <libgap/records.h>
#include <libgap/precord.h>
#include <libgap/cyclotom.h>
#include <libgap/vars.h>
#include <libgap/bool.h>
#include <libgap/libgap.h>
// in gasman.c but not declared in gasman.h
extern libGAP_Bag *                   libGAP_StopBags;
extern libGAP_Bag *                   libGAP_EndBags;
// vars.c
libGAP_Obj libGAP_FuncGetBottomLVars( libGAP_Obj );
#else
# define StackBottomBags libGAP_StackBottomBags
# include "libgap.h"
# ifndef CONFIGNAME
#  define CONFIGNAME "sage"
# endif

#include "libGAP.h"
libGAP_Obj libGAP_FuncGetBottomLVars( libGAP_Obj );

#endif

#if 0 // old variant

#if SIZEOF_VOID_P == 8
# define libGAP_SYS_IS_64_BIT          1
#elif !defined(SIZEOF_VOID_P)
# error Something is wrong with this GAP installation: SIZEOF_VOID_P not defined
#endif

//cdef extern from "libgap/system.h":
/* 64 bit machines -- well alphas anyway                                   */
#ifdef libGAP_SYS_IS_64_BIT
typedef char                    libGAP_Char;
typedef signed char             libGAP_Int1;
typedef short int               libGAP_Int2;
typedef int                     libGAP_Int4;
typedef long int                libGAP_Int8;
typedef long int                libGAP_Int;
typedef unsigned char           libGAP_UChar;
typedef unsigned char           libGAP_UInt1;
typedef unsigned short int      libGAP_UInt2;
typedef unsigned int            libGAP_UInt4;
typedef unsigned long int       libGAP_UInt8;
typedef unsigned long int       libGAP_UInt;

/* 32bit machines                                                          */
#else
typedef char                    libGAP_Char;
typedef signed char             libGAP_Int1;
typedef short int               libGAP_Int2;
typedef long int                libGAP_Int4;
typedef long int                libGAP_Int;
typedef long long int           libGAP_Int8;
typedef unsigned char           libGAP_UChar;
typedef unsigned char           libGAP_UInt1;
typedef unsigned short int      libGAP_UInt2;
typedef unsigned long int       libGAP_UInt4;
typedef unsigned long int       libGAP_UInt;
typedef unsigned long long int  libGAP_UInt8;

#endif

//cdef extern from "libgap/code.h":
typedef unsigned int libGAP_Stat;
typedef libGAP_Stat* libGAP_PtrBody;

// cdef extern from "libgap/gap.h":
typedef unsigned long int libGAP_UInt;
// from system.h
typedef libGAP_UInt * *        libGAP_Bag;
#define libGAP_Obj             libGAP_Bag
typedef libGAP_UInt libGAP_ExecStatus;

void libGAP_ViewObjHandler(void*x);
void libGAP_InitializeGap(int* argc, char** argv);
// void libGAP_set_system_variables(char**a, char**b);

extern libGAP_UInt libGAP_Last;
extern libGAP_UInt libGAP_Last2;
extern libGAP_UInt libGAP_Last3;

#define libGAP_STATUS_END         0
#define libGAP_STATUS_RETURN_VAL  1
#define libGAP_STATUS_RETURN_VOID 2
#define libGAP_STATUS_TNM         4
#define libGAP_STATUS_QUIT        8
#define libGAP_STATUS_EOF        16
#define libGAP_STATUS_ERROR      32
#define libGAP_STATUS_QQUIT      64

// #include <gap/objects.h>
#define libGAP_LAST_EXTERNAL_TNUM      libGAP_T_WPOBJ
#define libGAP_ADDR_OBJ(bag)        libGAP_PTR_BAG(bag)
//#define libGAP_LAST_REAL_TNUM          libGAP_LAST_EXTERNAL_TNUM
#define libGAP_LAST_VIRTUAL_TNUM libGAP_LAST_EXTERNAL_TNUM

#define libGAP_IS_FFE(o)               \
                        ((libGAP_Int)(o) & 0x02)
#define libGAP_IS_INTOBJ(o) \
    ((libGAP_Int)(o) & 0x01)
#define libGAP_INTOBJ_INT(i) \
    ((libGAP_Obj)(((libGAP_Int)(i) << 2) + 0x01))
#define libGAP_TNUM_OBJ(obj)   (libGAP_IS_INTOBJ( obj ) ? libGAP_T_INT : \
                         (libGAP_IS_FFE( obj ) ? libGAP_T_FFE : libGAP_TNUM_BAG( obj )))
#define libGAP_TNAM_OBJ(obj)   (libGAP_InfoBags[libGAP_TNUM_OBJ(obj)].name)
// typedef void* libGAP_Obj;
#define libGAP_SHALLOW_COPY_OBJ(obj) \
                        ((*libGAP_ShallowCopyObjFuncs[ libGAP_TNUM_OBJ(obj) ])( obj ))
#if HAVE_ARITHRIGHTSHIFT
#define libGAP_INT_INTOBJ(o) \
    ((libGAP_Int)(o) >> 2)
#else
#define libGAP_INT_INTOBJ(o) \
    (((libGAP_Int)(o)-1) / 4)
#endif
#define libGAP_ARE_INTOBJS(o1,o2) \
    ((libGAP_Int)(o1) & (libGAP_Int)(o2) & 0x01)

#define libGAP_LAST_REAL_TNUM          libGAP_LAST_EXTERNAL_TNUM
// what is this?
// from objects.h
#define libGAP_FIRST_REAL_TNUM 0
#define libGAP_FIRST_CONSTANT_TNUM 0
enum {
  libGAP_T_INT = libGAP_FIRST_CONSTANT_TNUM,
  libGAP_T_INTPOS,
  libGAP_T_INTNEG,
  libGAP_T_RAT,
  libGAP_T_CYC,
  libGAP_T_FFE,
  libGAP_T_PERM2,
  libGAP_T_PERM4,
  libGAP_T_BOOL,
  libGAP_T_CHAR,
  libGAP_T_FUNCTION,
  libGAP_T_FLAGS,
  libGAP_T_MACFLOAT,
  libGAP_T_LVARS,
  libGAP_T_SINGULAR,
  libGAP_T_POLYMAKE,
  libGAP_T_SPARE1,
  libGAP_T_SPARE2,
  libGAP_T_SPARE3,
  libGAP_T_SPARE4
};
#define libGAP_LAST_CONSTANT_TNUM      (libGAP_T_SPARE4)
#define libGAP_IMMUTABLE               1

#define libGAP_FIRST_IMM_MUT_TNUM      (libGAP_LAST_CONSTANT_TNUM+1)    /* Should be even */
#define libGAP_FIRST_RECORD_TNUM       libGAP_FIRST_IMM_MUT_TNUM
#define libGAP_T_PREC                  (libGAP_FIRST_RECORD_TNUM+ 0)
#define libGAP_LAST_RECORD_TNUM        (libGAP_T_PREC+libGAP_IMMUTABLE)
#define libGAP_FIRST_LIST_TNUM         (libGAP_LAST_RECORD_TNUM+1)

#define libGAP_FIRST_PLIST_TNUM        libGAP_FIRST_LIST_TNUM
#define libGAP_T_PLIST                  (libGAP_FIRST_LIST_TNUM+ 0)
#define libGAP_T_PLIST_NDENSE           (libGAP_FIRST_LIST_TNUM+ 2)
#define libGAP_T_PLIST_DENSE            (libGAP_FIRST_LIST_TNUM+ 4)
#define libGAP_T_PLIST_DENSE_NHOM       (libGAP_FIRST_LIST_TNUM+ 6)
#define libGAP_T_PLIST_DENSE_NHOM_SSORT (libGAP_FIRST_LIST_TNUM+ 8)
#define libGAP_T_PLIST_DENSE_NHOM_NSORT (libGAP_FIRST_LIST_TNUM+10)
#define libGAP_T_PLIST_EMPTY            (libGAP_FIRST_LIST_TNUM+12)
#define libGAP_T_PLIST_HOM              (libGAP_FIRST_LIST_TNUM+14)
#define libGAP_T_PLIST_HOM_NSORT        (libGAP_FIRST_LIST_TNUM+16)
#define libGAP_T_PLIST_HOM_SSORT        (libGAP_FIRST_LIST_TNUM+18)
#define libGAP_T_PLIST_TAB              (libGAP_FIRST_LIST_TNUM+20)
#define libGAP_T_PLIST_TAB_NSORT        (libGAP_FIRST_LIST_TNUM+22)
#define libGAP_T_PLIST_TAB_SSORT        (libGAP_FIRST_LIST_TNUM+24)
#define libGAP_T_PLIST_TAB_RECT         (libGAP_FIRST_LIST_TNUM+26)
#define libGAP_T_PLIST_TAB_RECT_NSORT   (libGAP_FIRST_LIST_TNUM+28)
#define libGAP_T_PLIST_TAB_RECT_SSORT   (libGAP_FIRST_LIST_TNUM+30)
#define libGAP_T_PLIST_CYC              (libGAP_FIRST_LIST_TNUM+32)
#define libGAP_T_PLIST_CYC_NSORT        (libGAP_FIRST_LIST_TNUM+34)
#define libGAP_T_PLIST_CYC_SSORT        (libGAP_FIRST_LIST_TNUM+36)
#define libGAP_T_PLIST_FFE              (libGAP_FIRST_LIST_TNUM+38)
#define libGAP_LAST_PLIST_TNUM          (libGAP_T_PLIST_FFE+libGAP_IMMUTABLE)
#define libGAP_T_RANGE_NSORT            (libGAP_FIRST_LIST_TNUM+40)
#define libGAP_T_RANGE_SSORT            (libGAP_FIRST_LIST_TNUM+42)
#define libGAP_T_BLIST                  (libGAP_FIRST_LIST_TNUM+44)
#define libGAP_T_BLIST_NSORT            (libGAP_FIRST_LIST_TNUM+46)
#define libGAP_T_BLIST_SSORT            (libGAP_FIRST_LIST_TNUM+48)
#define libGAP_T_STRING                 (libGAP_FIRST_LIST_TNUM+50)
#define libGAP_T_STRING_NSORT           (libGAP_FIRST_LIST_TNUM+52)
#define libGAP_T_STRING_SSORT           (libGAP_FIRST_LIST_TNUM+54)
#define libGAP_LAST_LIST_TNUM           (libGAP_T_STRING_SSORT+libGAP_IMMUTABLE)
#define libGAP_LAST_IMM_MUT_TNUM       libGAP_LAST_LIST_TNUM

#define libGAP_FIRST_EXTERNAL_TNUM     (libGAP_LAST_LIST_TNUM+1)
enum{
  libGAP_T_COMOBJ = libGAP_FIRST_EXTERNAL_TNUM,
  libGAP_T_POSOBJ,
  libGAP_T_DATOBJ,
  libGAP_T_WPOBJ
};

// #include <gap/read.h>
libGAP_UInt libGAP_ReadEvalCommand(libGAP_Obj context);
libGAP_UInt libGAP_ReadEvalFile();

extern libGAP_Obj libGAP_ReadEvalResult;
// extern libGAP_Obj ReadEvalResult;
// int libGAP_READ_ERROR();

// #include <gap/scanner.h>
void libGAP_ClearError();
//libGAP_UInt libGAP_NrError;
extern libGAP_UInt libGAP_Symbol;
void libGAP_GetSymbol();
void libGAP_Match(libGAP_UInt symbol, char* msg, libGAP_UInt skipto);
#define libGAP_S_TRUE          ((1UL<<11)+0)
#define libGAP_S_FALSE         ((1UL<<11)+1)
#define libGAP_S_CHAR          ((1UL<<11)+2)
#define libGAP_S_STRING        ((1UL<<11)+3)
#define libGAP_S_PARTIALSTRING ((1UL<<11)+4)

#define libGAP_S_REC           ((1UL<<12))

#define libGAP_S_FUNCTION      ((1UL<<13))
#define libGAP_S_LOCAL         ((1UL<<14))
#define libGAP_S_END           ((1UL<<15))
#define libGAP_S_MAPTO         ((1UL<<16))

#define libGAP_S_MULT          ((1UL<<17)+0)
#define libGAP_S_DIV           ((1UL<<17)+1)
#define libGAP_S_MOD           ((1UL<<17)+2)
#define libGAP_S_POW           ((1UL<<17)+3)

#define libGAP_S_PLUS          ((1UL<<18)+0)
#define libGAP_S_MINUS         ((1UL<<18)+1)

#define libGAP_S_EQ            ((1UL<<19)+0)
#define libGAP_S_LT            ((1UL<<19)+1)
#define libGAP_S_GT            ((1UL<<19)+2)
#define libGAP_S_NE            ((1UL<<19)+3)
#define libGAP_S_LE            ((1UL<<19)+4)
#define libGAP_S_GE            ((1UL<<19)+5)
#define libGAP_S_IN            ((1UL<<19)+6)

#define libGAP_S_NOT           ((1UL<<20)+0)
#define libGAP_S_AND           ((1UL<<20)+1)
#define libGAP_S_OR            ((1UL<<20)+2)

#define libGAP_S_ASSIGN        ((1UL<<21))

#define libGAP_S_IF            ((1UL<<22)+0)
#define libGAP_S_FOR           ((1UL<<22)+1)
#define libGAP_S_WHILE         ((1UL<<22)+2)
#define libGAP_S_REPEAT        ((1UL<<22)+3)

#define libGAP_S_THEN          ((1UL<<23))
#define libGAP_S_ELIF          ((1UL<<24)+0)
#define libGAP_S_ELSE          ((1UL<<24)+1)
#define libGAP_S_FI            ((1UL<<25))
#define libGAP_S_DO            ((1UL<<26))
#define libGAP_S_OD            ((1UL<<27))
#define libGAP_S_UNTIL         ((1UL<<28))

#define libGAP_S_BREAK         ((1UL<<29)+0)
#define libGAP_S_RETURN        ((1UL<<29)+1)
#define libGAP_S_QUIT          ((1UL<<29)+2)
#define libGAP_S_QQUIT         ((1UL<<29)+3)
#define libGAP_S_CONTINUE      ((1UL<<29)+4)

#define libGAP_S_SEMICOLON     ((1UL<<30))

#define libGAP_S_EOF           ((1UL<<31))

// #include <gap/gvars.h>
libGAP_UInt libGAP_GVarName(char* name);
void libGAP_AssGVar(libGAP_UInt gvar, libGAP_Obj val);
extern  libGAP_Obj *           libGAP_PtrGVars;
#define libGAP_VAL_GVAR(gvar)          libGAP_PtrGVars[ (gvar) ]

// #include <gap/string.h>
#define libGAP_CSTR_STRING(list)            ((libGAP_Char*)libGAP_ADDR_OBJ(list) + sizeof(libGAP_UInt))
#define libGAP_CHARS_STRING(list)           ((libGAP_UChar*)libGAP_ADDR_OBJ(list) + sizeof(libGAP_UInt))
#define libGAP_GET_LEN_STRING(list)         (*((libGAP_UInt*)libGAP_ADDR_OBJ(list)))
#define libGAP_SET_LEN_STRING(list,len)     (*((libGAP_UInt*)libGAP_ADDR_OBJ(list)) = (libGAP_UInt)(len))
#define libGAP_IS_STRING(obj)  ((*libGAP_IsStringFuncs[ libGAP_TNUM_OBJ( obj ) ])( obj ))
extern  libGAP_Int             (*libGAP_IsStringFuncs [libGAP_LAST_REAL_TNUM+1]) ( libGAP_Obj obj );

libGAP_Obj libGAP_NEW_STRING(libGAP_Int len); // sic!

#define libGAP_C_NEW_STRING(string,len,cstr) \
  do { \
    size_t tmp_len = (len); \
    string = libGAP_NEW_STRING( tmp_len ); \
    memcpy( libGAP_CHARS_STRING(string), (cstr), tmp_len ); \
  } while ( 0 );


// gap/gasman.h
void libGAP_InitGlobalBag(libGAP_Obj* addr, char* cookie);
#define libGAP_CHANGED_BAG(bag)                                                    \
                if (   libGAP_PTR_BAG(bag) <= libGAP_YoungBags                              \
                  && libGAP_PTR_BAG(bag)[-1] == (bag) ) {                          \
                    libGAP_PTR_BAG(bag)[-1] = libGAP_ChangedBags; libGAP_ChangedBags = (bag);    }
extern libGAP_UInt libGAP_NrAllBags;
extern libGAP_UInt libGAP_SizeAllBags;
extern libGAP_UInt libGAP_NrLiveBags;
extern libGAP_UInt libGAP_SizeLiveBags;
extern libGAP_UInt libGAP_NrDeadBags;
extern libGAP_UInt libGAP_SizeDeadBags;
extern libGAP_UInt libGAP_NrHalfDeadBags;
libGAP_UInt libGAP_CollectBags(libGAP_UInt size, libGAP_UInt full);
void libGAP_CallbackForAllBags(void (*func)(libGAP_Obj));
// libGAP_Char* libGAP_TNAM_BAG(libGAP_Bag obj);

// #include <gap/gasman.h>
#ifdef libGAP_USE_NEWSHAPE
#define libGAP_TNUM_BAG(bag)  (*(*(bag)-2) & 0xFFFFL)
#define libGAP_SIZE_BAG(bag)   (*(*(bag)-2) >> 16)
#else
#define libGAP_TNUM_BAG(bag)   (*(*(bag)-3))
#define libGAP_SIZE_BAG(bag)   (*(*(bag)-2))
#endif
typedef struct  {
    const libGAP_Char *            name;
    libGAP_UInt                    nrLive;
    libGAP_UInt                    nrAll;
    libGAP_UInt                    sizeLive;
    libGAP_UInt                    sizeAll;
} libGAP_TNumInfoBags;

extern  libGAP_TNumInfoBags            libGAP_InfoBags [ 256 ];
#define libGAP_PTR_BAG(bag)    (*(libGAP_Bag**)(bag))
void libGAP_CheckMasterPointers();

// gasman.c
// in gasman.c but not declared in gasman.h
extern libGAP_Bag *                   libGAP_YoungBags;
extern libGAP_UInt                    libGAP_AllocSizeBags;
extern libGAP_Bag *                   libGAP_StopBags;
extern libGAP_Bag *                   libGAP_EndBags;

//gasman.h
extern  libGAP_Bag *                   libGAP_MptrBags;
extern  libGAP_Bag *                   libGAP_OldBags;
extern  libGAP_Bag *                   libGAP_AllocBags;
extern  libGAP_Bag                     libGAP_MarkedBags;

#define libGAP_MARKED_DEAD(x)  (x)
#define libGAP_MARKED_ALIVE(x) ((libGAP_Bag)(((libGAP_Char *)(x))+1))
#define libGAP_MARKED_HALFDEAD(x) ((libGAP_Bag)(((libGAP_Char *)(x))+2))
#define libGAP_IS_MARKED_ALIVE(bag) ((libGAP_PTR_BAG(bag)[-1]) == libGAP_MARKED_ALIVE(bag))
#define libGAP_IS_MARKED_DEAD(bag) ((libGAP_PTR_BAG(bag)[-1]) == libGAP_MARKED_DEAD(bag))
#define libGAP_IS_MARKED_HALFDEAD(bag) ((libGAP_PTR_BAG(bag)[-1]) == libGAP_MARKED_HALFDEAD(bag))
#define libGAP_UNMARKED_DEAD(x)  (x)
#define libGAP_UNMARKED_ALIVE(x) ((libGAP_Bag)(((libGAP_Char *)(x))-1))
#define libGAP_UNMARKED_HALFDEAD(x) ((libGAP_Bag)(((libGAP_Char *)(x))-2))


#define libGAP_MARK_BAG(bag)                                                       \
                if ( (((libGAP_UInt)((intptr_t)bag)) & (sizeof(libGAP_Bag)-1)) == 0                 \
                  && (libGAP_Bag)libGAP_MptrBags <= (bag)    && (bag) < (libGAP_Bag)libGAP_OldBags      \
                  && (intptr_t)libGAP_YoungBags < (intptr_t)libGAP_PTR_BAG(bag) \
                  && (intptr_t)libGAP_PTR_BAG(bag) <= (intptr_t)libGAP_AllocBags \
                  && (libGAP_IS_MARKED_DEAD(bag) || libGAP_IS_MARKED_HALFDEAD(bag)) ) \
                  {                                                          \
                    libGAP_PTR_BAG(bag)[-1] = libGAP_MarkedBags; libGAP_MarkedBags = (bag);      }


// #include <gap/ariths.h>
#define libGAP_QUO(opL,opR)    ((*libGAP_QuoFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR))
#define libGAP_SUM(opL,opR)    ((*libGAP_SumFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR))
#define libGAP_MOD(opL,opR)    ((*libGAP_ModFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR))
#define libGAP_POW(opL,opR)    ((*libGAP_PowFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR))
#define libGAP_DIFF(opL,opR)   ((*libGAP_DiffFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR))
#define libGAP_PROD(opL,opR)   ((*libGAP_ProdFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR))
typedef libGAP_Obj (* libGAP_ArithMethod2) ( libGAP_Obj opL, libGAP_Obj opR );
extern libGAP_ArithMethod2 libGAP_QuoFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
extern libGAP_ArithMethod2 libGAP_ModFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
extern libGAP_ArithMethod2 libGAP_ProdFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
extern libGAP_ArithMethod2 libGAP_DiffFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
extern libGAP_ArithMethod2 libGAP_SumFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
extern libGAP_ArithMethod2 libGAP_PowFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];

extern libGAP_Obj libGAP_QuoOper;
typedef libGAP_Int (* libGAP_CompaMethod) ( libGAP_Obj opL, libGAP_Obj opR );
extern libGAP_CompaMethod libGAP_EqFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
extern libGAP_CompaMethod libGAP_LtFuncs [libGAP_LAST_VIRTUAL_TNUM+1][libGAP_LAST_VIRTUAL_TNUM+1];
#define libGAP_EQ(opL,opR)     ((opL) == (opR) || \
                         (!libGAP_ARE_INTOBJS(opL,opR) && \
                          (*libGAP_EqFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR)))
#define libGAP_LT(opL,opR)     ((opL) == (opR) ? 0 : \
                         (libGAP_ARE_INTOBJS(opL,opR) ? (libGAP_Int)(opL) < (libGAP_Int)(opR) : \
                          (*libGAP_LtFuncs[libGAP_TNUM_OBJ(opL)][libGAP_TNUM_OBJ(opR)])(opL,opR)))


// #include <gap/calls.h>
#define libGAP_IS_FUNC(obj)    (libGAP_TNUM_OBJ(obj) == libGAP_T_FUNCTION)

// #include <gap/plist.h>
#define libGAP_NEW_PLIST(type,plen)            libGAP_NewBag(type,((plen)+1)*sizeof(libGAP_Obj))
#define libGAP_LEN_PLIST(list)                 ((libGAP_Int)(libGAP_ADDR_OBJ(list)[0]))
#define libGAP_IS_PLIST( list ) \
  (libGAP_FIRST_PLIST_TNUM <= libGAP_TNUM_OBJ(list) && libGAP_TNUM_OBJ(list) <= libGAP_LAST_PLIST_TNUM)
#define libGAP_SET_ELM_PLIST(list, pos, val) do { libGAP_Obj sep_Obj = (val); libGAP_ADDR_OBJ(list)[pos] = sep_Obj; } while (0)
#define libGAP_ELM_PLIST(list,pos)             (libGAP_ADDR_OBJ(list)[pos])
typedef libGAP_Obj (* libGAP_ObjFunc) (/*arguments*/);
#define libGAP_HDLR_FUNC(func,i)       (* (libGAP_ObjFunc*) (libGAP_ADDR_OBJ(func) + 0 +(i)) )

//#include <gap/calls.h>
#define libGAP_CALL_0ARGS(f)                     libGAP_HDLR_FUNC(f,0)(f)
#define libGAP_CALL_1ARGS(f,a1)                  libGAP_HDLR_FUNC(f,1)(f,a1)
#define libGAP_CALL_2ARGS(f,a1,a2)               libGAP_HDLR_FUNC(f,2)(f,a1,a2)
#define libGAP_CALL_3ARGS(f,a1,a2,a3)            libGAP_HDLR_FUNC(f,3)(f,a1,a2,a3)
#define libGAP_CALL_4ARGS(f,a1,a2,a3,a4)         libGAP_HDLR_FUNC(f,4)(f,a1,a2,a3,a4)
#define libGAP_CALL_5ARGS(f,a1,a2,a3,a4,a5)      libGAP_HDLR_FUNC(f,5)(f,a1,a2,a3,a4,a5)
#define libGAP_CALL_6ARGS(f,a1,a2,a3,a4,a5,a6)   libGAP_HDLR_FUNC(f,6)(f,a1,a2,a3,a4,a5,a6)
#define libGAP_CALL_XARGS(f,as)                  libGAP_HDLR_FUNC(f,7)(f,as)
// #include <gap/gap.h>
// #include <gap/lists.h>
// void libGAP_UNB_LIST(libGAP_Obj list, int pos);

void libGAP_AddList(libGAP_Obj list, libGAP_Obj obj);
void libGAP_AddPlist(libGAP_Obj list, libGAP_Obj obj);

// #include <gap/records.h>
extern  libGAP_Obj             libGAP_NamesRNam;
#define libGAP_NAME_RNAM(rnam) libGAP_CSTR_STRING( libGAP_ELM_PLIST( libGAP_NamesRNam, rnam ) )
libGAP_UInt libGAP_RNamIntg(int i);
libGAP_UInt libGAP_RNamName(libGAP_Char* name);

#define libGAP_ELM_REC(rec,rnam) \
                        ((*libGAP_ElmRecFuncs[ libGAP_TNUM_OBJ(rec) ])( rec, rnam ))
extern  libGAP_Obj             (*libGAP_ElmRecFuncs[libGAP_LAST_REAL_TNUM+1]) ( libGAP_Obj rec, libGAP_UInt rnam );

#define libGAP_IS_REC(obj)     ((*libGAP_IsRecFuncs[ libGAP_TNUM_OBJ(obj) ])( obj ))
extern  libGAP_Int             (*libGAP_IsRecFuncs[libGAP_LAST_REAL_TNUM+1]) ( libGAP_Obj obj );

// #include <gap/precord.h>
libGAP_Obj libGAP_NEW_PREC(int len); // sic!
#define libGAP_LEN_PREC(rec)   (((libGAP_UInt *)(libGAP_ADDR_OBJ(rec)))[1])
#define libGAP_GET_RNAM_PREC(rec,i) \
                        (*(libGAP_UInt*)(libGAP_ADDR_OBJ(rec)+2*(i)))
#define libGAP_GET_ELM_PREC(rec,i) \
                        (*(libGAP_ADDR_OBJ(rec)+2*(i)+1))
void libGAP_AssPRec(libGAP_Obj rec, libGAP_UInt rnam, libGAP_Obj val);
void libGAP_UnbPRec(libGAP_Obj rec, libGAP_UInt rnam);
int libGAP_IsbPRec(libGAP_Obj rec, libGAP_UInt rnam);
libGAP_Obj libGAP_ElmPRec(libGAP_Obj rec, libGAP_UInt rnam);

//cdef extern from "libgap/cyclotom.h":
//    pass

// #include <gap/bool.h>
extern libGAP_Obj libGAP_True;
extern libGAP_Obj libGAP_False;

// #include <gap/code.h>
// #include <gap/vars.h>
extern libGAP_Obj libGAP_BottomLVars;

// hmmm
// #define libGAP_BottomLVars BottomLVars

libGAP_Obj libGAP_FuncGetBottomLVars( void* );

// just gasman
// #define libGAP_StackBottomBags StackBottomBags

#endif // ! HAVE_LIBGAP
#endif
