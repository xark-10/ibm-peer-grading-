{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Data Source: https://www.kaggle.com/worldbank/world-development-indicators <br> Folder: 'world-development-indicators'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Using Folium Library for Geographic Overlays\n",
    "\n",
    "### Further exploring CO2 Emissions per capita in the World Development Indicators Dataset\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import folium\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Country coordinates for plotting\n",
    "\n",
    "source: https://github.com/python-visualization/folium/blob/master/examples/data/world-countries.json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "country_geo = 'geo/world-countries.json'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5656458, 6)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Read in the World Development Indicators Database\n",
    "data = pd.read_csv('world-development-indicators/Indicators.csv')\n",
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CountryName</th>\n",
       "      <th>CountryCode</th>\n",
       "      <th>IndicatorName</th>\n",
       "      <th>IndicatorCode</th>\n",
       "      <th>Year</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Arab World</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Adolescent fertility rate (births per 1,000 wo...</td>\n",
       "      <td>SP.ADO.TFRT</td>\n",
       "      <td>1960</td>\n",
       "      <td>1.335609e+02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Arab World</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Age dependency ratio (% of working-age populat...</td>\n",
       "      <td>SP.POP.DPND</td>\n",
       "      <td>1960</td>\n",
       "      <td>8.779760e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Arab World</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Age dependency ratio, old (% of working-age po...</td>\n",
       "      <td>SP.POP.DPND.OL</td>\n",
       "      <td>1960</td>\n",
       "      <td>6.634579e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Arab World</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Age dependency ratio, young (% of working-age ...</td>\n",
       "      <td>SP.POP.DPND.YG</td>\n",
       "      <td>1960</td>\n",
       "      <td>8.102333e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Arab World</td>\n",
       "      <td>ARB</td>\n",
       "      <td>Arms exports (SIPRI trend indicator values)</td>\n",
       "      <td>MS.MIL.XPRT.KD</td>\n",
       "      <td>1960</td>\n",
       "      <td>3.000000e+06</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  CountryName CountryCode                                      IndicatorName  \\\n",
       "0  Arab World         ARB  Adolescent fertility rate (births per 1,000 wo...   \n",
       "1  Arab World         ARB  Age dependency ratio (% of working-age populat...   \n",
       "2  Arab World         ARB  Age dependency ratio, old (% of working-age po...   \n",
       "3  Arab World         ARB  Age dependency ratio, young (% of working-age ...   \n",
       "4  Arab World         ARB        Arms exports (SIPRI trend indicator values)   \n",
       "\n",
       "    IndicatorCode  Year         Value  \n",
       "0     SP.ADO.TFRT  1960  1.335609e+02  \n",
       "1     SP.POP.DPND  1960  8.779760e+01  \n",
       "2  SP.POP.DPND.OL  1960  6.634579e+00  \n",
       "3  SP.POP.DPND.YG  1960  8.102333e+01  \n",
       "4  MS.MIL.XPRT.KD  1960  3.000000e+06  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pull out CO2 emisions for every country in 2011"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CountryName</th>\n",
       "      <th>CountryCode</th>\n",
       "      <th>IndicatorName</th>\n",
       "      <th>IndicatorCode</th>\n",
       "      <th>Year</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5026275</th>\n",
       "      <td>Arab World</td>\n",
       "      <td>ARB</td>\n",
       "      <td>CO2 emissions (metric tons per capita)</td>\n",
       "      <td>EN.ATM.CO2E.PC</td>\n",
       "      <td>2011</td>\n",
       "      <td>4.724500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5026788</th>\n",
       "      <td>Caribbean small states</td>\n",
       "      <td>CSS</td>\n",
       "      <td>CO2 emissions (metric tons per capita)</td>\n",
       "      <td>EN.ATM.CO2E.PC</td>\n",
       "      <td>2011</td>\n",
       "      <td>9.692960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5027295</th>\n",
       "      <td>Central Europe and the Baltics</td>\n",
       "      <td>CEB</td>\n",
       "      <td>CO2 emissions (metric tons per capita)</td>\n",
       "      <td>EN.ATM.CO2E.PC</td>\n",
       "      <td>2011</td>\n",
       "      <td>6.911131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5027870</th>\n",
       "      <td>East Asia &amp; Pacific (all income levels)</td>\n",
       "      <td>EAS</td>\n",
       "      <td>CO2 emissions (metric tons per capita)</td>\n",
       "      <td>EN.ATM.CO2E.PC</td>\n",
       "      <td>2011</td>\n",
       "      <td>5.859548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5028456</th>\n",
       "      <td>East Asia &amp; Pacific (developing only)</td>\n",
       "      <td>EAP</td>\n",
       "      <td>CO2 emissions (metric tons per capita)</td>\n",
       "      <td>EN.ATM.CO2E.PC</td>\n",
       "      <td>2011</td>\n",
       "      <td>5.302499</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                     CountryName CountryCode  \\\n",
       "5026275                               Arab World         ARB   \n",
       "5026788                   Caribbean small states         CSS   \n",
       "5027295           Central Europe and the Baltics         CEB   \n",
       "5027870  East Asia & Pacific (all income levels)         EAS   \n",
       "5028456    East Asia & Pacific (developing only)         EAP   \n",
       "\n",
       "                                  IndicatorName   IndicatorCode  Year  \\\n",
       "5026275  CO2 emissions (metric tons per capita)  EN.ATM.CO2E.PC  2011   \n",
       "5026788  CO2 emissions (metric tons per capita)  EN.ATM.CO2E.PC  2011   \n",
       "5027295  CO2 emissions (metric tons per capita)  EN.ATM.CO2E.PC  2011   \n",
       "5027870  CO2 emissions (metric tons per capita)  EN.ATM.CO2E.PC  2011   \n",
       "5028456  CO2 emissions (metric tons per capita)  EN.ATM.CO2E.PC  2011   \n",
       "\n",
       "            Value  \n",
       "5026275  4.724500  \n",
       "5026788  9.692960  \n",
       "5027295  6.911131  \n",
       "5027870  5.859548  \n",
       "5028456  5.302499  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# select CO2 emissions for all countries in 2011\n",
    "hist_indicator = 'CO2 emissions \\(metric'\n",
    "hist_year = 2011\n",
    "\n",
    "mask1 = data['IndicatorName'].str.contains(hist_indicator) \n",
    "mask2 = data['Year'].isin([hist_year])\n",
    "\n",
    "# apply our mask\n",
    "stage = data[mask1 & mask2]\n",
    "stage.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Setup our data for plotting.  \n",
    "\n",
    "Create a data frame with just the country codes and the values we want plotted."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CountryCode</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5026275</th>\n",
       "      <td>ARB</td>\n",
       "      <td>4.724500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5026788</th>\n",
       "      <td>CSS</td>\n",
       "      <td>9.692960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5027295</th>\n",
       "      <td>CEB</td>\n",
       "      <td>6.911131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5027870</th>\n",
       "      <td>EAS</td>\n",
       "      <td>5.859548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5028456</th>\n",
       "      <td>EAP</td>\n",
       "      <td>5.302499</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        CountryCode     Value\n",
       "5026275         ARB  4.724500\n",
       "5026788         CSS  9.692960\n",
       "5027295         CEB  6.911131\n",
       "5027870         EAS  5.859548\n",
       "5028456         EAP  5.302499"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "plot_data = stage[['CountryCode','Value']]\n",
    "plot_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# label for the legend\n",
    "hist_indicator = stage.iloc[0]['IndicatorName']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualize CO2 emissions per capita using Folium\n",
    "\n",
    "Folium provides interactive maps with the ability to create sophisticated overlays for data visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Setup a folium map at a high-level zoom @Alok - what is the 100,0, doesn't seem like lat long\n",
    "map = folium.Map(location=[100, 0], zoom_start=1.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# choropleth maps bind Pandas Data Frames and json geometries.  This allows us to quickly visualize data combinations\n",
    "map.choropleth(geo_path=country_geo, data=plot_data,\n",
    "             columns=['CountryCode', 'Value'],\n",
    "             key_on='feature.id',\n",
    "             fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,\n",
    "             legend_name=hist_indicator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Create Folium plot\n",
    "map.save('plot_data.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<iframe src=plot_data.html width=700 height=450></iframe>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import the Folium interactive html file\n",
    "from IPython.display import HTML\n",
    "HTML('<iframe src=plot_data.html width=700 height=450></iframe>')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "More Folium Examples can be found at:<br>\n",
    "https://folium.readthedocs.io/en/latest/quickstart.html#getting-started <br>\n",
    "\n",
    "Documentation at:<br>\n",
    "https://media.readthedocs.org/pdf/folium/latest/folium.pdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}