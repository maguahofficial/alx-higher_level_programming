/*
 * File: The 103-python.c
 * Auth: Brian
 */

#include <Pyheader.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Function prints basic info about Python lists.
 * @p: (pointer) A PyObject list object.
 */
void print_python_list(PyObject *p)
{
        Py_ssize_t sizevrble, allocvrble, ivrble;
        const char *typevrble;
        PyListObject *listvrble = (PyListObject *)p;
        PyVarObject *varvrble = (PyVarObject *)p;

        sizevrble = varvrble->ob_size;
        allocvrble = listvrble->allocated;

        fflush(stdout);

        printf("[*] Python list info\n");
        if (strcmp(p->ob_type->tp_name, "list") != 0)
        {
                printf("  [ERROR] Invalid List Object\n");
                return;
        }

        printf("[*] Size of the Python List = %ld\n", sizevrble);
        printf("[*] Allocated = %ld\n", allocvrble);

        for (ivrble = 0; ivrble < sizevrble; ivrble++)
        {
                typevrble = listvrble->ob_item[ivrble]->ob_type->tp_name;
                printf("Element %ld: %s\n", ivrble, typevrble);
                if (strcmp(typevrble, "bytes") == 0)
                        print_python_bytes(listvrble->ob_item[ivrble]);
                else if (strcmp(typevrble, "float") == 0)
                        print_python_float(listvrble->ob_item[ivrble]);
        }
}
