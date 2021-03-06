{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "768f43ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2.8.6 (dt dec pq3 ext lo64)'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import psycopg2\n",
    "psycopg2.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3bff60c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>goutham</td>\n",
       "      <td>boine</td>\n",
       "      <td>12000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>harish</td>\n",
       "      <td>varanasi</td>\n",
       "      <td>20000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tejaswi</td>\n",
       "      <td>malla</td>\n",
       "      <td>18000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>rishi</td>\n",
       "      <td>diban</td>\n",
       "      <td>18000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>paresh</td>\n",
       "      <td>dvs</td>\n",
       "      <td>25000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>pavan</td>\n",
       "      <td>goshika</td>\n",
       "      <td>30000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>venkat</td>\n",
       "      <td>chowdary</td>\n",
       "      <td>10000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>sirisha</td>\n",
       "      <td>vimula</td>\n",
       "      <td>35000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  first_name last_name   salary\n",
       "0    goutham     boine  12000.0\n",
       "1     harish  varanasi  20000.0\n",
       "2    tejaswi     malla  18000.0\n",
       "3      rishi     diban  18000.0\n",
       "4     paresh       dvs  25000.0\n",
       "5      pavan   goshika  30000.0\n",
       "6     venkat  chowdary  10000.0\n",
       "7    sirisha    vimula  35000.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "dbString = \"postgresql://postgres:sunny123@localhost:5432/postgre_flask\"\n",
    "\n",
    "connection = create_engine(dbString).connect()\n",
    "\n",
    "data = pd.read_sql_table(\"employee\", connection)\n",
    "\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "18892062",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>goutham</td>\n",
       "      <td>boine</td>\n",
       "      <td>12000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>harish</td>\n",
       "      <td>varanasi</td>\n",
       "      <td>20000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tejaswi</td>\n",
       "      <td>malla</td>\n",
       "      <td>18000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>rishi</td>\n",
       "      <td>diban</td>\n",
       "      <td>18000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>paresh</td>\n",
       "      <td>dvs</td>\n",
       "      <td>25000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>pavan</td>\n",
       "      <td>goshika</td>\n",
       "      <td>30000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>venkat</td>\n",
       "      <td>chowdary</td>\n",
       "      <td>10000.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>sirisha</td>\n",
       "      <td>vimula</td>\n",
       "      <td>35000.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  first_name last_name   salary\n",
       "0    goutham     boine  12000.0\n",
       "1     harish  varanasi  20000.0\n",
       "2    tejaswi     malla  18000.0\n",
       "3      rishi     diban  18000.0\n",
       "4     paresh       dvs  25000.0\n",
       "5      pavan   goshika  30000.0\n",
       "6     venkat  chowdary  10000.0\n",
       "7    sirisha    vimula  35000.0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(data)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "cf460edc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "plt.plot(df.first_name,df[\"salary\"])\n",
    "plt.title(\"salary plotting\")\n",
    "plt.xlabel(\"person name\")\n",
    "plt.ylabel(\"salaries\")\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1cfa3a7",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
