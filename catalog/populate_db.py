# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Book

import datetime

engine = create_engine('postgresql:///catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create categories

arts = Category(name='Arts & Photography')
biographies = Category(name='Biographies & Memoirs')
classics = Category(name='Classics')
fantasy = Category(name='Fantasy')
horror = Category(name='Horror')
historical = Category(name='Historical Fiction')
mystery = Category(name='Mystery, Thriller & Suspense')
scifi = Category(name='Science Fiction')
travel = Category(name='Travel')
ya = Category(name='Young Adult')

# Add some books

arts.books = [
    Book(title='The Art of Photography: An Approach to Personal Expression',
    	author='Bruce Barnbaum',
    	publisher='Rocky Nook',
    	published=datetime.date(2010, 12, 8),
    	description='This is an updated and newly revised edition of the classic book The Art of Photography (originally published in 1994), which has often been described as the most readable, understandable, and complete textbook on photography. With well over 100 beautiful photographic illustrations in both black-and-white and color, as well as numerous charts, graphs, and tables, this book presents the world of photography to beginner, intermediate, and advanced photographers seeking to make a personal statement through the medium of photography. Without talking down to anyone, or talking over anyone\'s head, Barnbaum presents "how to" techniques for both traditional and digital approaches. Yet he goes well beyond the technical, as he delves deeply into the philosophical, expressive, and creative aspects of photography so often avoided in other books.')
]

biographies.books = [
    Book(title='Philip K. Dick: The Last Interview',
    	author='Philip K. Dick',
    	publisher='Melville House',
    	published=datetime.date(2015, 12, 15),
    	description='Long before Ridley Scott transformed Do Androids Dream of Electric Sheep? into Blade Runner, Philip K. Dick was banging away at his typewriter in relative obscurity, ostracized by the literary establishment. Today he is widely considered one of the most influential writers of the 20th century. These interviews reveal a man plagued by bouts of manic paranoia and failed suicide attempts; a career fuelled by alcohol, amphetamines, and mystical inspiration; and, above all, a magnificent and generous imagination at work.')
]

classics.books = [
    Book(title='The Great Gatsby',
    	author='F. Scott Fitzgerald',
    	publisher='Charles Scribner\'s Sons',
    	published=datetime.date(1925, 4, 25),
    	description='The Great Gatsby is a 1925 novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the fictional town of West Egg on prosperous Long Island in the summer of 1922. The story primarily concerns the young and mysterious millionaire Jay Gatsby and his quixotic passion and obsession for the beautiful former debutante Daisy Buchanan. Considered to be Fitzgerald\'s magnum opus, The Great Gatsby explores themes of decadence, idealism, resistance to change, social upheaval, and excess, creating a portrait of the Jazz Age or the Roaring Twenties that has been described as a cautionary tale regarding theAmerican Dream. ')
]

fantasy.books = [
    Book(title='Gardens of the Moon',
    	author='Steven Erikson',
    	publisher='Transworld Digital',
    	published=datetime.date(2009, 7, 28),
    	description='Bled dry by interminable warfare, infighting and bloody confrontations with Lord Anomander Rake and his Tiste Andii, the vast, sprawling Malazan empire simmers with discontent. Even its imperial legions yearn for some respite. For Sergeant Whiskeyjack and his Bridgeburners and for Tattersail, sole surviving sorceress of the Second Legion, the aftermath of the siege of Pale should have been a time to mourn the dead. But Darujhistan, last of the Free Cities of Genabackis, still holds out - and Empress Lasseen\'s ambition knows no bounds. However, it seems the empire is not alone in this great game. Sinister forces gather as the gods themselves prepare to play their hand...')
]

horror.books = [
    Book(title='The Bazaar of Bad Dreams',
    	author='Stephen King',
    	publisher='Hodder & Stoughton',
    	published=datetime.date(2015, 11, 3),
    	description='A generous collection of thrilling stories - some brand new, some published in magazines, all entirely brilliant and assembled in one book for the first time - with a wonderful bonus: in addition to his introduction to the whole collection, King gives readers a fascinating introduction to each story with autobiographical comments on their origins and motivation...')
]

historical.books =[
    Book(title='All the Light We Cannot See',
    	author='Anthony Doerr',
    	publisher='Fourth Estate',
    	published=datetime.date(2014, 5, 6),
    	description='A beautiful, stunningly ambitious novel about a blind French girl and a German boy whose paths collide in occupied France as both try to survive the devastation of World War II. Marie-Laure has been blind since the age of six. Her father builds a perfect miniature of their Paris neighbourhood so she can memorize it by touch and navigate her way home. But when the Nazis invade, father and daughter flee with a dangerous secret. Werner is a German orphan, destined to labour in the same mine that claimed his father’s life, until he discovers a knack for engineering. His talent wins him a place at a brutal military academy, but his way out of obscurity is built on suffering. At the same time, far away in a walled city by the sea, an old man discovers new worlds without ever setting foot outside his home. But all around him, impending danger closes in.')
]

mystery.books = [
    Book(title='NYPD Red 4',
    	author='James Patterson',
    	publisher='Little, Brown and Company',
    	published=datetime.date(2016, 1, 25),
    	description='It\'s another glamorous night in the heart of Manhattan: at a glitzy movie premiere, a gorgeous starlet, dressed to the nines and dripping in millions of dollars\' worth of jewelry on loan, makes her way past a horde of fans and paparazzi. But then there\'s a sudden loud noise, an even louder scream, and a vicious crime with millions of witnesses and no suspect--and now NYPD Red has a new case on its hands. NYPD Red: the elite task force assigned to protect the rich, famous, and connected in the city where crime never sleeps. Detective Zach Jordan and his partner, Kylie MacDonald--a former girlfriend from the police academy who he hasn\'t quite gotten over--are the best that Red has to offer, brilliant and tireless investigators who will stop at nothing to crack a case, even if it means putting their own complicated lives on the back burner.')
]

scifi.books = [
    Book(title='Dune',
    	author='Frank Herbert',
    	publisher='Chilton Books',
    	published=datetime.date(1965, 8, 1),
    	description='The Duke of Atreides has been manoeuvred by his arch-enemy, Baron Harkonnen, into administering the desert planet of Dune. Although it is almost completely without water, Dune is a planet of fabulous wealth, for it is the only source of a drug prized throughout the Galactic Empire. The Duke and his son, Paul, are expecting treachery, and it duly comes - but from a shockingly unexpected place. Then Paul succeeds his father, and he becomes a catalyst for the native people of Dune, whose knowledge of the ecology of the planet gives them vast power. They have been waiting for a leader like Paul Atreides, a leader who can harness that force ...')
]

travel.books = [
    Book(title='Walking the Nile',
    	author='Levison Wood',
    	publisher='Atlantic Monthly Press',
    	published=datetime.date(2016, 2, 2),
    	description='The Nile, one of the world’s great rivers, has long been an object of fascination and obsession. From Alexander the Great and Nero, to Victorian adventurers David Livingstone, John Hanning Speke, and Henry Morton Stanley, the river has seduced men and led them into wild adventures. English writer, photographer, and explorer Levison Wood is just the latest. His Walking the Nile is a captivating account of a remarkable and unparalleled Nile journey. Starting in November 2013 in a forest in Rwanda, where a modest spring spouts a trickle of clear, cold water, Wood set forth on foot, aiming to become the first person to walk the entire length of the fabled river. He followed the Nile for nine months, over 4,000 miles, through six nations—Rwanda, Tanzania, Uganda, South Sudan, the Republic of Sudan, and Egypt—to the Mediterranean coast.')
]

ya.books = [
    Book(title='Ender\'s Game',
    	author='Orson Scott Card',
    	publisher='Tor Books',
    	published=datetime.date(1985, 1, 15),
    	description='In order to develop a secure defense against a hostile alien race\'s next attack, government agencies breed child geniuses and train them as soldiers. A brilliant young boy, Andrew "Ender" Wiggin lives with his kind but distant parents, his sadistic brother Peter, and the person he loves more than anyone else, his sister Valentine. Peter and Valentine were candidates for the soldier-training program but didn\'t make the cut--young Ender is the Wiggin drafted to the orbiting Battle School for rigorous military training. Ender\'s skills make him a leader in school and respected in the Battle Room, where children play at mock battles in zero gravity. Yet growing up in an artificial community of young soldiers, Ender suffers greatly from isolation, rivalry from his peers, pressure from the adult teachers, and an unsettling fear of the alien invaders. His psychological battles include loneliness, fear that he is becoming like the cruel brother he remembers, and fanning the flames of devotion to his beloved sister. Is Ender the general Earth needs? But Ender is not the only result of the genetic experiments. The war with the Buggers has been raging for a hundred years, and the quest for the perfect general has been underway for almost as long. Ender\'s two older siblings are every bit as unusual as he is, but in very different ways. Between the three of them lie the abilities to remake a world. If the world survives, that is.')
]

# Save to database

session.add_all(
	[
	    arts,
	    biographies,
	    classics,
	    fantasy,
	    horror,
	    historical,
	    mystery,
	    scifi,
	    travel,
	    ya
	]
)

session.commit()



