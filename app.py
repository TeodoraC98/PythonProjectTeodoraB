
from flask import Flask, render_template, request, redirect, url_for,json,jsonify
from models import Tour_Datastore, Tour, Path_Img_Tour, Path_Img_Datastore, Attraction
from favourite_db import Favourite_Tour_DB
app = Flask(__name__)

# create the tours Tour_Datastore() object  to access the tours information
tour_datastore=Tour_Datastore()
path_img_tour_datastore=Path_Img_Datastore()
# crate the Favourite_Tour_DB() for saving the informations
favourite_db=Favourite_Tour_DB()
# The lines below are all the information necessary that i need in my project but i need to store them with a shelve


atr_rome=Attraction({"About city":"Rome, historic city and capital of Roma provincia (province),of Lazio regione (region), and of the country of Italy.Once the capital of an ancient republic and empire whose armies and polity defined the Western world in antiquity and left  seemingly indelible imprints thereafter, the spiritual and physical seat of the Roman Catholic Church, and the site of major pinnacles of artistic and intellectual achievement,"
                           "Rome is the Eternal City, remaining today a political capital, a religious centre, and a memorial to the creative imagination of the past."
                         "Via del Corso and environs The main street in central Rome is the Via del Corso, an important thoroughfare since Classical times, when it was the Via Flaminia, the road to the Adriatic. Its present name comes from the horse races (corse) that were part of the Roman carnival celebrations. From the foot of the Capitoline Hill, the Corso runs to the Piazza del Popolo and through a gate in the city wall, the Porta del Popolo, there to resume its ancient name.",
                         "Colosseum":"The Colosseum  is an elliptical amphitheatre in the centre of the city of Rome, Italy, just east of the Roman Forum. It is the largest ancient amphitheatre ever built, and is still the largest standing amphitheatre in the world, despite its age. Construction began under the emperor Vespasian  in 72 and was completed in AD 80 under his successor and heir, Titus "
                           ".Further modifications were made during the reign of Domitian.",
                           "Sistine Chapel":"The Sistine Chapel is a chapel in the Apostolic Palace, the pope's official residence in Vatican City. Originally known as the Cappella Magna ('Great Chapel'), the chapel takes its name from Pope Sixtus IV, who had it built between 1473 and 1481. Since that time, the chapel has served as a place of both religious and functionary papal activity. Today, it is the site of the papal conclave, the process by which a new pope is selected. The fame of the Sistine Chapel lies mainly in the frescoes that decorate the interior, most particularly the Sistine Chapel ceiling and The Last Judgment, both by Michelangelo."
                           "Between 1508 and 1512, under the patronage of Pope Julius II, Michelangelo painted the chapel's ceiling, a project that changed the course of Western art and is regarded as one of the major artistic accomplishments of human civilization."})
atr_bucharest=Attraction({"Palace of Parliament":"The Palace of the Parliament (Romanian: Palatul Parlamentului), also known as the House of the Republic or People's "
"House/People's Palace, is the seat of the Parliament of Romania, located atop Dealul Spirii in Bucharest, the national capital."
 "The Palace reaches a height of 84m, has a floor area of 365,000 m2 and a volume of 2,550,000 m3."
"The Palace of the Parliament is one of the heaviest buildings in the world, weighing about 4,098,500 tonnes, also being the second"
" largest administrative building in the world. The building was designed and  supervised by chief architect Anca Petrescu, with a team of approximately 700 architects,"
"and constructed over a period of 13 years (1984–97) in modernist Neoclassical architectural forms and styles, with socialist realism in mind. The Palace was ordered by Nicolae"
 "Ceaușescu (1918–1989), the president of Communist Romania and the second of two long-ruling "
"heads of state in the country since World War II, during a period in which the personality" 
"cult of political worship and adoration increased considerably for him and his family.",
"Lipscani":"Lipscani is a street and a district of Bucharest, Romania, which from the Middle Ages to the early 19th century was the most important commercial area of the city and Wallachia. It is located near the ruins of the old Princely Court built by Vlad III the Impaler."
"It was named after Leipzig (Lipsca in 17th century Romanian), as that was the origin of many of the wares that could be found on the main street. The word lipscan (singular of lipscani) meant trader who brought his wares from Western Europe.",
"The Little Paris Museum":"WELL HIDDEN IN THE HEART of Old Town lies a treasure trove that carries visitors back to Bucharest’s golden age. The museum is nestled in a house that once belonged to a wealthy family of Greek descent."
"Originally opened by master photographer Eugen Ciocan, the museum is a fusion between an antique gallery, cafe, and a retro photo studio. It was designed as an escape from the modern, fast-paced world back to a fabulous era of elegance and decadence. "
"This museum celebrates the history of Bucharest, also known as Little Paris, and its splendid interiors pay homage to the two main influences that defined Bucharest at the time: Byzantinian and French."})
atr_florence=Attraction({"City":"Florence, city, capital of Firenze provincia (province) and Toscana (Tuscany) regione, central Italy. The city, located about 145 miles (230 km) northwest of Rome,"
 "is surrounded by gently rolling hills that are covered with villas and farms, vineyards, and orchards. Florence was founded as a Roman military colony about the 1st century BCE,"
 "and during its long history it has been a republic, a seat of the duchy of Tuscany, and a capital (1865–70) of Italy. During the 14th–16th century Florence achieved preeminence in commerce and finance, learning, and especially the arts."
 " Among the most famous of the city’s cultural giants are Leonardo da Vinci, Michelangelo, Dante, Machiavelli, Galileo, and its most-renowned rulers, generations of the Medici family.",
 "Piazzale Michelangelo":"Piazzale Michelangelo (Michelangelo Square) is a square with a panoramic view of Florence, Italy, located in the Oltrarno district."
 "The square, dedicated to the Renaissance sculptor Michelangelo, has bronze copies of some of his marble works found elsewhere in Florence: the David and the four allegories of the times of day at the |Medici Chapel of San Lorenzo.",
 "Gallerie Degli Uffizi":"The Uffizi Gallery is a prominent art museum located adjacent to the Piazza della Signoria in the Historic Centre of Florence in the region of Tuscany, Italy. One of the most important Italian museums and the most visited, it is also one of the largest and best-known in the world and holds a collection of priceless works, particularly from the period of the Italian Renaissance."
"After the ruling House of Medici died out, their art collections were given to the city of Florence under the famous Patto di famiglia negotiated by Anna Maria Luisa, the last Medici heiress. The Uffizi is one of the first modern museums. The gallery had been open to visitors by request since the sixteenth century, and in 1769 it was officially opened to the public, formally becoming a museum in 1865",
"Duomo - Cattedrale di Santa Maria del Fiore":"Florence Cathedral, formally the Cathedral of Saint Mary of the Flower, is the cathedral of Florence, Italy. It was begun in 1296 in the Gothic style to a design of Arnolfo di Cambio and was structurally completed by 1436, with the dome engineered by Filippo Brunelleschi. The exterior of the basilica is faced with polychrome marble panels in various shades of green and pink,"
"bordered by white, and has an elaborate 19th-century Gothic Revival façade by Emilio De Fabris.The cathedral complex, in Piazza del Duomo, includes the Baptistery and Giotto's Campanile. These three buildings are part of the UNESCO World Heritage Site covering the historic centre of Florence and are a major tourist attraction of Tuscany. The basilica is one of Italy's largest "
"churches, and until the development of new structural materials in the modern era, the dome was the largest in the world. It remains the largest brick dome ever constructed.The cathedral is the mother church of the Archdiocese of Florence, whose archbishop is Giuseppe Betori." })
atr_amsterdam=Attraction({"Anne Frank House":"The Anne Frank House (Dutch: Anne Frank Huis) is a writer's house and biographical museum dedicated to Jewish wartime diarist Anne Frank. The building is located on a canal called the Prinsengracht, close to the Westerkerk, in central Amsterdam in the Netherlands."
"During World War II, when the Netherlands was occupied by Germany, Anne Frank hid from Nazi persecution with her family and four other people in hidden rooms, in the rear building, of the 17th-century canal house, later known as the Secret Annex. She did not survive the war but her wartime diary was published in 1947."
 "Ten years later the Anne Frank Foundation was established to protect the property from developers who wanted to demolish the block.",
 "Van Gogh Museum":"The Van Gogh Museum is a Dutch art museum dedicated to the works of Vincent van Gogh and his contemporaries in the Museum Square in Amsterdam South, close to the Stedelijk Museum, the Rijksmuseum, and the Concertgebouw. The museum opened on 2 June 1973, and its buildings were designed by Gerrit Rietveld and Kisho Kurokawa."
"The museum contains the largest collection of Van Gogh's paintings and drawings in the world. In 2017, the museum had 2.3 million visitors and was the most-visited museum in the Netherlands, and the 23rd-most-visited art museum in the world. In 2019, the Van Gogh Museum launched the Meet Vincent Van Gogh Experience, a technology-driven (immersive exhibition) on Van Gogh's life and works, which has toured globally."})
atr_paris=Attraction({
   "City":"Paris is especially known for its museums and architectural landmarks: the Louvre received 8.9. million visitors in 2023, on track for keeping its position as the most-visited art museum in the world."
"The Musée d'Orsay, Musée Marmottan Monet and Musée de l'Orangerie are noted for their collections of French Impressionist art. The Pompidou Centre Musée National d'Art Moderne, Musée Rodin and Musée Picasso are noted for their collections of modern and contemporary art. The historical district along the Seine in the city centre has been classified as a UNESCO World Heritage Site since 1991.",
   "The Louvre":"The Louvre or the Louvre Museum, is a national art museum in Paris, France. It is located on the Right Bank of the Seine in the city's 1st arrondissement (district or ward) and home to some of the most canonical works "
"of Western art, including the Mona Lisa and the Venus de Milo. The museum is housed in the Louvre Palace, originally built in the late 12th to 13th century under Philip II. Remnants of the Medieval Louvre fortress"
"are visible in the basement of the museum. Due to urban expansion, the fortress eventually lost its defensive function, and in 1546 Francis I converted it into the primary residence of the French Kings."
"The museum opened on 10 August 1793 with an exhibition of 537 paintings, the majority of the works being royal and confiscated church property. Because of structural problems with the building, the museum was closed from 1796 until 1801. The collection was increased under Napoleon and the museum was renamed Musée Napoléon,"
"but after Napoleon's abdication, many works seized by his armies were returned to their original owners. The collection was further increased during the reigns of Louis XVIII and Charles X, and during the Second French Empire the museum gained 20,000 pieces.",
    "Eiffel Tower":"The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower from 1887 to 1889."
"Locally nicknamed La dame de fer (French for Iron Lady), it was constructed as the centerpiece of the 1889 World's Fair, and to crown the centennial anniversary of the French Revolution."
"Although initially criticised by some of France's leading artists and intellectuals for its design, it has since become a global cultural icon of France and one of the most recognisable structures"
"in the world. The tower received 5,889,000 visitors in 2022.The Eiffel Tower is the most visited monument with an entrance fee in the world: 6.91 million people ascended it in 2015. It was designated a monument historique in 1964, and was named part of a UNESCO World Heritage Site (Paris, Banks of the Seine) in 1991.",
      "Disneyland Paris":"Disneyland Paris is an entertainment resort in Chessy, France, 32 kilometres east of Paris. It encompasses two theme parks, resort hotels, a shopping, dining and entertainment complex, and a golf course. Disneyland Park is the original theme park of the complex, opening in 1992. A second theme park, Walt Disney Studios Park, opened in 2002. Disneyland Paris celebrated its 30th anniversary in 2022; "
 "by then 375 million people had visited, making it the most visited theme park in Europe.It is the second Disney park outside the United States, following the opening of the Tokyo Disney Resort in 1983, and the largest. Disneyland Paris is also the only Disney resort outside of the United States to be completely owned by The Walt Disney Company. It includes seven hotels: Disney Hotel Santa Fe, Disney Hotel Cheyenne, Sequoia Lodge, Newport Bay Club, Hotel New York – the Art of Marvel, The Disneyland Hotel, and Davy Crockett Ranch."
})
atr_dublin=Attraction({
   "City":"Dublin is the capital and largest city of Ireland.On a bay at the mouth of the River Liffey, it is in the province of Leinster, bordered on the south by the Dublin Mountains, a part of the Wicklow Mountains range. At the 2022 census, the city council area had a population of 592,713, while Dublin City and its suburbs had a population of 1,263,219, and County Dublin had a population of 1,501,500."
"A settlement was established in the area by the Gaels during or before the 7th century, followed by the Vikings. As the Kingdom of Dublin grew, it became Ireland's principal settlement by the 12th century Anglo-Norman invasion of Ireland. The city expanded rapidly from the 17th century and was briefly the second largest in the British Empire and sixth largest in Western Europe after the Acts of Union in 1800."
"Following independence in 1922, Dublin became the capital of the Irish Free State, renamed Ireland in 1937.",
"The Little Museum of Dublin":"As a local history museum for the city of Dublin, the Little Museum chronicles the history of the city in the 20th century. It provides visitors with information on life in Dublin during that time period. "
"The museum has a collection of over 5,000 artefacts that have been donated or loaned directly from the people of Dublin. It has three floors of exhibition space in the Georgian townhouse and one floor for office space. Exhibitions in the museum include displays covering the 1916 Rising, U.S. President John F. Kennedy's visit to Dublin, and many other events in Irish political and social history. In 2014 the museum opened an exhibit that focuses on the rock band U2.",
"Guinness Storehouse":"Guinness Storehouse is a tourist attraction at St. James's Gate Brewery in Dublin, Ireland. Since opening in 2000, it has received over twenty million visitors."
"The Storehouse covers seven floors surrounding a glass atrium shaped in the form of a pint of Guinness. The ground floor introduces the beer's four ingredients (water, barley, hops and yeast), and the brewery's founder, Arthur Guinness. Other floors feature the history of Guinness advertising and include an interactive exhibit on responsible drinking. The seventh floor houses the Gravity Bar with views of Dublin and where visitors may drink a pint of Guinness included in the price of admission.",
"Kilmainham Gaol Museum":"Kilmainham Gaol is a former prison in Kilmainham, Dublin, Ireland. It is now a museum run by the Office of Public Works, an agency of the Government of Ireland. Many Irish revolutionaries, including the leaders of the 1916 Easter Rising, were imprisoned and executed in the prison by the orders of the UK Government."})
atr_barcelona=Attraction({
   "City":"Barcelona is a city on the northeastern coast of Spain. It is the capital and largest city of the autonomous community of Catalonia, as well as the second-most populous municipality of Spain. With a population of 1.6 million within city limits."
"Founded as a Roman city, in the Middle Ages Barcelona became the capital of the County of Barcelona. After joining with the Kingdom of Aragon to form the confederation of the Crown of Aragon, Barcelona, which continued to be the capital of the Principality of Catalonia, "
"became the most important city in the Crown of Aragon and the main economic and administrative centre of the Crown, only to be overtaken by Valencia, wrested from Moorish control by the Catalans, shortly before the dynastic union between the Crown of Castile and the Crown of Aragon "
"in 1492. Barcelona became the centre of Catalan separatism, briefly becoming part of France during the 17th century Reapers' War. It was the capital of Revolutionary Catalonia during the Spanish Revolution of 1936, and the seat of government of the Second Spanish Republic later in the Spanish Civil War, until its capture by the fascists in 1939. After the Spanish transition to democracy in the 1970s, Barcelona once again became the capital of an autonomous Catalonia."
"Barcelona has a rich cultural heritage and is today an important cultural centre and a major tourist destination. Particularly renowned are the architectural works of Antoni Gaudí and Lluís Domènech i Montaner, which have been designated UNESCO World Heritage Sites",
    "Basílica de la Sagrada Familia":"The Basílica i Temple Expiatori de la Sagrada Família, otherwise known as Sagrada Família, is a church under construction in the Eixample district of Barcelona, Catalonia, Spain. It is the largest unfinished Catholic church in the world. Designed by Catalan architect Antoni Gaudí (1852–1926), his work on Sagrada Família is part of a UNESCO World Heritage Site. On 7 November 2010, Pope Benedict XVI consecrated the church and proclaimed it a minor basilica."
"On 19 March 1882, construction of the Sagrada Família began under architect Francisco de Paula del Villar. In 1883, when Villar resigned, Gaudí took over as chief architect, transforming the project with his architectural and engineering style, combining Gothic and curvilinear Art Nouveau forms. Gaudí devoted the remainder of his life to the project, and he is buried in the church's crypt. At the time of his death in 1926, less than a quarter of the project was complete.",
"Casa Batlló":"Casa Batlló  is a building in the center of Barcelona, Spain. It was designed by Antoni Gaudí, and is considered one of his masterpieces. A remodel of a previously built house, it was redesigned in 1904 by Gaudí and has been refurbished several times after that. Gaudí's assistants Domènec Sugrañes i Gras, Josep Canaleta and Joan Rubió also contributed to the renovation project."
"The local name for the building is Casa dels ossos (House of Bones), as it has a visceral, skeletal organic quality. It is located on the Passeig de Gràcia in the Eixample district, and forms part of a row of houses known as the Illa de la Discòrdia (or Mansana de la Discòrdia, the Block of Discord), which consists of four buildings by noted Modernista architects of Barcelona."
"Like everything Gaudí designed, Casa Batlló is only identifiable as Modernisme in the broadest sense. The ground floor, in particular, has unusual tracery, irregular oval windows and flowing sculpted stone work. There are few straight lines, and much of the façade is decorated with a colorful mosaic made of broken ceramic tiles (trencadís). The roof is arched and was likened to the back of a dragon or dinosaur. A common theory"
"about the building is that the rounded feature to the left of centre, terminating at the top in a turret and cross, represents the lance of Saint George, which has been plunged into the back of the dragon."})
atr_milan=Attraction({
   "City":"Milan is a city in Northern Italy, regional capital of Lombardy, and the second-most populous city proper in Italy after Rome. The city proper has a population of about 1.4 million."
   "Milan is a leading alpha global city, with strengths in the fields of art, chemicals, commerce, design, education, entertainment, fashion, finance, healthcare, media (communication), services, research and tourism. "
   "Milan has been recognized as one of the world's four fashion capitals. Many of the most famous luxury fashion brands in the world have their headquarters in the city, including: Armani, Prada, Versace, Moschino, Valentino and Zegna. It also hosts several international events and fairs, including Milan Fashion Week and the Milan Furniture Fair, which are among the world's biggest in terms of revenue, visitors and growth",
   "Duomo di Milano":" Lombardy, Italy. Dedicated to the Nativity of St. Mary (Santa Maria Nascente), it is the seat of the Archbishop of Milan, currently Archbishop Mario Delpini."
"The cathedral took nearly six centuries to complete: construction began in 1386, and the final details were completed in 1965. It is the largest church in the Italian Republic—the larger St. Peter's Basilica is in the State of Vatican City"
})
# print(k)
# for key in k:
#    print(obiective_rome.get_tr_spots()[key])
tour_datastore.add_tour(Tour("id_rome","Rome","static/images/rome/rome.jpg","560",5,atr_rome))
tour_datastore.add_tour(Tour("id_bucharest","Bucharest","static/images/bucharest/bucharest.jpg",350,4,atr_bucharest))
tour_datastore.add_tour(Tour("id_florence","Florence","static/images/florence/florence.jpg",730,8,atr_florence))
tour_datastore.add_tour(Tour("id_amsterdam","Amsterdam","static/images/amsterdam/amsterdam.jpg","560",5,atr_amsterdam))
tour_datastore.add_tour(Tour("id_paris","Paris","static/images/paris/paris.jpg",350,4,atr_paris))
tour_datastore.add_tour(Tour("id_dublin","Dublin","static/images/dublin/dublin.jpg",730,8,atr_dublin))
tour_datastore.add_tour(Tour("id_milan","Milan","static/images/milan/milan.jpg",350,4,atr_milan))
tour_datastore.add_tour(Tour("id_barcelona","Barcelona","static/images/barcelona/barcelona.jpg",730,8,atr_barcelona))


a=(Path_Img_Tour("id_rome",(("static/images/rome/rome1.jpg",
                                                                "static/images/rome/rome2.jpg",
                                                                "static/images/rome/rome3.jpg",
                                                         ))))
                                                                
b=(Path_Img_Tour("id_bucharest",(("static/images/bucharest/bucharest1.jpg",
                                                                "static/images/bucharest/bucharest2.jpg",
                                                                "static/images/bucharest/bucharest3.jpg",
                                                                "static/images/bucharest/bucharest4.jpg"))))
c=(Path_Img_Tour("id_amsterdam",(("static/images/amsterdam/amsterdam1.jpg","static/images/amsterdam/amsterdam2.jpg"))))
d=(Path_Img_Tour("id_barcelona",(("static/images/barcelona/barcelona_1.jpg",
                                                                "static/images/barcelona/barcelona_2.jpg",
                                                                "static/images/barcelona/barcelona_3.jpg"  ))))
f=(Path_Img_Tour("id_dublin",(("static/images/dublin/dublin_1.jpg",
                                                                "static/images/dublin/dublin_2.jpg",
                                                                "static/images/dublin/dublin_3.jpg",
                                                                "static/images/dublin/dublin_4.jpg"))))
g=(Path_Img_Tour("id_florence",(("static/images/florence/florence_1.jpg",
                                                                "static/images/florence/florence_2.jpg"))))
h=(Path_Img_Tour("id_milan",(("static/images/milan/milan_1.jpg",
                                                                "static/images/milan/milan_2.jpg"))))
i=(Path_Img_Tour("id_paris",(("static/images/paris/paris_1.jpg",
                                                                "static/images/paris/paris_2.jpg",
                                                                "static/images/paris/paris_3.jpg",
                                                                "static/images/paris/paris_4.jpg"))))
path_img_tour_datastore.add_path_tour(a)
path_img_tour_datastore.add_path_tour(b)
path_img_tour_datastore.add_path_tour(c)
path_img_tour_datastore.add_path_tour(d)
path_img_tour_datastore.add_path_tour(f)
path_img_tour_datastore.add_path_tour(g)
path_img_tour_datastore.add_path_tour(h)
path_img_tour_datastore.add_path_tour(i)

suggestion_tours={"id_rome":"static/images/rome/rome3.jpg",
                       "id_florence":"static/images/florence/florence_2.jpg",
                       "id_dublin":"static/images/dublin/dublin_3.jpg",
                       "id_milan":"static/images/milan/milan_1.jpg",
                       "id_paris":"static/images/paris/paris_1.jpg",
                        "id_portugal":"static/images/banner/sunsetportugal.jpeg"}

# when the client access the home page they receive the list of tours that we provide
# and the tours that they mark like favorites
@app.route("/")
def home():
    return render_template("home.html", tours=tour_datastore.get_tours(), fav_tours=favourite_db.get_tours())

# the root for viewing the selected tour information
@app.route("/get_details_tour", methods=["post"])
def infomation_tour():
#I'm getting the id of the tour from the form
   id_t=request.form["name"]
#   based on date i select the information from the tour_datastore
   tour_selected=tour_datastore.get_tour(id_t)
#    i select the paths for the pictures
   paths=path_img_tour_datastore.get_path_imgs_tour(id_t)
   paths=paths.get_path_imgs()
# I'm getting the tours attraction from the class Tour
   tourist_attraction=tour_selected.get_tourist_attraction().get_tr_spots()
#    the tourist attraction are storege in a dictionary and the key is the name of the attraction
 # I'm getting the names of the attractions
   keys=(tour_selected.get_tourist_attraction().get_tr_spots()).keys()  
   return render_template("information_tour.html",paths=paths,tour=tour_selected, tourist_attraction=tourist_attraction,keys=keys,suggestion_tours=suggestion_tours)
   
# when i select the button from the navigation bar  I'm redirect to the home page
@app.route("/tours", methods=["POST"])
def go_back_home():
    return redirect(url_for("home"))

# when i select the button FAVOURITES from the navigation bar I'm redirect to the view_fav_tours page that contains the list with the tours makes like favorite
# in this page i have a section with some suggestion tours that they are saved in a dictionary
@app.route("/view_fav_tours", methods=["POST","GET"])
def list_favourite_tours():
    #  check what method was called
     if request.method=="POST":
      return render_template("favourite.html",favourite_tours=favourite_db.get_tours(),suggestion_tours=suggestion_tours)
     else:
      return render_template("favourite.html",favourite_tours=favourite_db.get_tours(),suggestion_tours=suggestion_tours)


@app.route("/set_favourite", methods=["POST"])
def set_tour_favourite():
       # get the id of the selected tour from the form
    id_tour=request.form["favourite_tour"]
    # im getting the tour base on id from the tour_datastore
    selected_tour=tour_datastore.get_tour(id_tour)
    # when we mark a tour as favourite the information for tour are saved in favourite_db
    favourite_db.add_favourite(selected_tour)
    return ('', 204)
   

@app.route("/delete_favourite", methods=["POST"])
def delete_fav_tour():
    # I'm receiving the id for the tour that need to be delete
    id_tour=request.form["delete_favourite_tour"]
    # i delete the tour from favourite_db
    favourite_db.delete_favourite_tour(id_tour)
    return ('', 204)
    




if __name__ == "__main__":
    app.run(debug=True, port=8080)