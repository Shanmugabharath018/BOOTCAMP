{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "abe7181d-b85d-4474-9739-a368cd6f9d4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Barks...\n",
      " sleepyyyyy...\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "    def __init__(self, name, age):\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "    def bark(self):\n",
    "        print(\"Barks...\")\n",
    "    def sleep(self):\n",
    "        print(\" sleepyyyyy...\")\n",
    "my_dog=Dog(\"daisy\",3)\n",
    "\n",
    "my_dog.bark()\n",
    "my_dog.sleep()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a5a1aa8-cfad-4691-8d3d-7455b23dbba0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
