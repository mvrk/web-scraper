## web-scraper

This web scraper can automatically process web pages and count keywords of a page.
This project take wikipedia webpages as target and count the 'citation needed' repeated time in a single page.

**Project requirments**: (from Labs)
- Module must be named scraper.py
- Create function named get_citations_needed_count
- takes in a url string and returns an integer.
- Create function named get_citations_needed_report
- takes in a url string and returns a report string
- the string should be formatted with each citation listed in the order found.


**Tools and Dependencies**

See [requirements.txt](./requirements.txt).

**How to use**

1, run ```web_scraper.py``` in your terminal;

2, follow the prompt to paste a wikipedia web URL;

3, hit enter to see the result.

**Sample test result**

- URL

```https://en.wikipedia.org/wiki/Mexico```

- Result
```
******************This link of page need 4 citations.*************************
******************The following paragraphs require citations******************
Mexico is crossed from north to south by two mountain ranges known as Sierra Madre Oriental and Sierra Madre Occidental, which are the extension of the Rocky Mountains from northern North America. From east to west at the center, the country is crossed by the Trans-Mexican Volcanic Belt also known as the Sierra Nevada. A fourth mountain range, the Sierra Madre del Sur, runs from Michoacán to Oaxaca. As such, the majority of the Mexican central and northern territories are located at high altitudes, and the highest elevations are found at the Trans-Mexican Volcanic Belt: Pico de Orizaba (5,700 m or 18,701 ft), Popocatépetl (5,462 m or 17,920 ft) and Iztaccihuatl (5,286 m or 17,343 ft) and the Nevado de Toluca (4,577 m or 15,016 ft). Three major urban agglomerations are located in the valleys between these four elevations: Toluca, Greater Mexico City and Puebla.[citation needed] An important geologic feature of the Yucatán peninsula is the Chicxulub crater. The scientific consensus is that the Chicxulub impactor was responsible for the Cretaceous–Paleogene extinction event. Mexico is subject to a number of natural hazards, including hurricanes on both coasts, tsunamis on the Pacific coast, and volcanism.[147]

Mexico has 233 airports with paved runways; of these, 35 carry 97% of the passenger traffic.[citation needed] The Mexico City International Airport remains the busiest in Latin America and the 36th busiest in the world[300] transporting 45 million passengers a year.[301]

During the early 20th century, a substantial number of Arabs (mostly Christians)[citation needed] began arriving from the crumbling Ottoman Empire. The largest group were the Lebanese and an estimated 400,000 Mexicans have some Lebanese ancestry.[337]

In the 19th century the neoclassical movement arose as a response to the objectives of the republican nation, one of its examples are the Hospicio Cabañas where the strict plastic of the classical orders are represented in their architectural elements, new religious buildings also arise, civilian and military that demonstrate the presence of neoclassicism. Romanticists from a past seen through archeology show images of medieval Europe, Islamic and pre-Columbian Mexico in the form of architectural elements in the construction of international exhibition pavilions looking for an identity typical of the national culture. The art nouveau, and the art deco were styles introduced into the design of the Palacio de Bellas Artes to mark the identity of the Mexican nation with Greek-Roman and pre-Columbian symbols.[citation needed]

```
