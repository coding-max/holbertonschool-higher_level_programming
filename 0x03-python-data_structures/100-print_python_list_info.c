#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	PyListObject *list_obj;
	int  list_size, i = 0;
	/* print size of the list and allocations */
	list_size = PyList_Size(p);
	list_obj = (PyListObject *)p;
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", (int)(list_obj->allocated));
	/* print elements of the list */
	while (i < list_size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
