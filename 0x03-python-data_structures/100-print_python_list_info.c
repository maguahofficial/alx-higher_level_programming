#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - The Function prints some basic
 * info about Python lists
 * @p: (pointer)python list
 */
void print_python_list_info(PyObject *p)
{
	int elemvrb;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elemvrb = 0; elemvrb < Py_SIZE(p); elemvrb++)
		printf("Element %d: %s\n", elemvrb, Py_TYPE(PyList_GetItem(p, elemvrb))->tp_name);
}

