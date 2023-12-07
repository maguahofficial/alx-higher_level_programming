#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - The function prints bytes information
 *  Python - More Data Structures: Set, Dictionary task
 * @p: (ointer) Python Object
 * Return: returns no return
 */
void print_python_bytes(PyObject *p)
{
	char *stringvarble;
	long int sizevarble, ivarble, limitvarble;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sizevarble = ((PyVarObject *)(p))->ob_size;
	stringvarble = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", sizevarble);
	printf("  trying string: %s\n", stringvarble);

	if (sizevarble >= 10)
		limitvarble = 10;
	else
		limitvarble = sizevarble + 1;

	printf("  first %ld bytes:", limitvarble);

	for (ivarble = 0; ivarble < limitvarble; ivarble++)
		if (stringvarble[i] >= 0)
			printf(" %02x", stringvarble[ivarble]);
		else
			printf(" %02x", 256 + stringvarble[ivarble]);

	printf("\n");
}

/**
 * print_python_list - The function Prints list information
 *  Python - More Data Structures: Set, Dictionary project
 * @p: (pointer) Python Object
 * Return: returns no return
 */
void print_python_list(PyObject *p)
{
	long int sizevarble, ivarble;
	PyListObject *listvarble;
	PyObject *objvarble;

	sizevarble = ((PyVarObject *)(p))->ob_size;
	listvarble = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sizevarble);
	printf("[*] Allocated = %ld\n", listvarble->allocated);

	for (ivarble = 0; ivarble < sizevarble; ivarble++)
	{
		objvarble = ((PyListObject *)p)->ob_item[ivarble];
		printf("Element %ld: %s\n", ivarble, ((objvarble)->ob_type)->tp_name);
		if (PyBytes_Check(objvarble))
			print_python_bytes(objvarble);
	}
