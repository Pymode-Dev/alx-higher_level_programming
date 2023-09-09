#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints hidden info about list operation
 * @p: PyObject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] size of the python list = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	i = 0;
	for (; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, PyTYPE(item)->tp_name);
	}
}
