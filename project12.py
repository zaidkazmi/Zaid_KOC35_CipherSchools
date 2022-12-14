{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e5a3f7b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 is valid.\n",
      "2 is valid.\n",
      "3 is valid.\n",
      "4 is not valid.\n",
      "5 is valid.\n",
      "6 is not valid.\n",
      "7 is not valid.\n",
      "8 is valid.\n",
      "9 is not valid.\n",
      "10 is not valid.\n",
      "11 is not valid.\n",
      "12 is not valid.\n",
      "13 is valid.\n",
      "14 is not valid.\n",
      "15 is not valid.\n",
      "16 is not valid.\n",
      "17 is not valid.\n",
      "18 is not valid.\n",
      "19 is not valid.\n",
      "20 is not valid.\n",
      "21 is valid.\n",
      "22 is not valid.\n",
      "23 is not valid.\n",
      "24 is not valid.\n",
      "25 is not valid.\n",
      "26 is not valid.\n",
      "27 is not valid.\n",
      "28 is not valid.\n",
      "29 is not valid.\n",
      "30 is not valid.\n",
      "31 is not valid.\n",
      "32 is not valid.\n",
      "33 is not valid.\n",
      "34 is valid.\n",
      "35 is not valid.\n",
      "36 is not valid.\n",
      "37 is not valid.\n",
      "38 is not valid.\n",
      "39 is not valid.\n",
      "40 is not valid.\n",
      "41 is not valid.\n",
      "42 is not valid.\n",
      "43 is not valid.\n",
      "44 is not valid.\n",
      "45 is not valid.\n",
      "46 is not valid.\n",
      "47 is not valid.\n",
      "48 is not valid.\n",
      "49 is not valid.\n",
      "50 is not valid.\n",
      "51 is not valid.\n",
      "52 is not valid.\n",
      "53 is not valid.\n",
      "54 is not valid.\n",
      "55 is valid.\n",
      "56 is not valid.\n",
      "57 is not valid.\n",
      "58 is not valid.\n",
      "59 is not valid.\n",
      "60 is not valid.\n",
      "61 is not valid.\n",
      "62 is not valid.\n",
      "63 is not valid.\n",
      "64 is not valid.\n",
      "65 is not valid.\n",
      "66 is not valid.\n",
      "67 is not valid.\n",
      "68 is not valid.\n",
      "69 is not valid.\n",
      "70 is not valid.\n",
      "71 is not valid.\n",
      "72 is not valid.\n",
      "73 is not valid.\n",
      "74 is not valid.\n",
      "75 is not valid.\n",
      "76 is not valid.\n",
      "77 is not valid.\n",
      "78 is not valid.\n",
      "79 is not valid.\n",
      "80 is not valid.\n",
      "81 is not valid.\n",
      "82 is not valid.\n",
      "83 is not valid.\n",
      "84 is not valid.\n",
      "85 is not valid.\n",
      "86 is not valid.\n",
      "87 is not valid.\n",
      "88 is not valid.\n",
      "89 is valid.\n",
      "90 is not valid.\n",
      "91 is not valid.\n",
      "92 is not valid.\n",
      "93 is not valid.\n",
      "94 is not valid.\n",
      "95 is not valid.\n",
      "96 is not valid.\n",
      "97 is not valid.\n",
      "98 is not valid.\n",
      "99 is not valid.\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    " \n",
    "def isPerfectSquare(x):\n",
    "\n",
    "    s = int(math.sqrt(x))\n",
    "\n",
    "    return s*s == x\n",
    " \n",
    "def isFibonacci(n):\n",
    "\n",
    "    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)\n",
    "\n",
    "for i in range(1,100):\n",
    "\n",
    "     if (isFibonacci(i) == True):\n",
    "\n",
    "         print(i,\"is valid.\")\n",
    "\n",
    "     else:\n",
    "\n",
    "         print(i,\"is not valid.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7374ead",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
