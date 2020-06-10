from lyrics import Lyrics


file_name = 'lyrics_fr/Feu_Zoe_short.txt'

language = 'fr'
print_stats = True
lookback = 30
l = Lyrics(file_name, print_stats=print_stats, 
                  language=language, lookback=lookback)

for rhyme in (sorted(l.rhyme_map.items(), key=lambda x: x[1])):
    print rhyme[0], rhyme[1]



