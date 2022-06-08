LEVELS = {1:'Kingdom', 2:'Phylum', 3:'Class', 4:'Order', 5:'Family', 6:'Genus', 7:'Species'}

def unquote(s):
    return(s[1:len(s)-1])

class PhyloSeqNAResolvePlugin:
    def input(self, filename):
       myfile = open(filename, 'r')
       self.firstline = myfile.readline()
       self.N = len(self.firstline.strip().split(','))
       self.contents = []
       for line in myfile:
           self.contents.append(line.strip().split(','))
       for i in range(len(self.contents)):
           self.contents[i][1] = self.contents[i][1].replace('d__', '')

    def run(self):
        for i in range(len(self.contents)):
             # First, change species to genus and species
             #if (len(self.contents[i]) > 7 and self.contents[i][7] != "\"NA\"" and (not self.contents[i][7].endswith('unclassified\"')) and (not self.contents[i][7].startswith('\"uncultured')) and self.contents[i][7] != "\"metagenome\"" and self.contents[i][7] != "\"gut_metagenome\"" and self.contents[i][7] != "\"unidentified\"" and self.contents[i][7] != "\"human_gut\""):
             #print(self.contents[i][7])
             #self.contents[i][7] = '\"' + unquote(self.contents[i][6])+" "+unquote(self.contents[i][7]) + '\"'
             #else:  # Species is NA.  Go back to the first position that is not
             pos2 = self.N-1
             #while (self.contents[i][pos] == "\"NA\"" or self.contents[i][pos].endswith('unclassified\"') or
             #         self.contents[i][pos].startswith('\"uncultured') or self.contents[i][pos] == "\"metagenome\"" or self.contents[i][pos] == "\"gut_metagenome\"" or self.contents[i][pos] == "\"unidentified\"" or self.contents[i][pos] == "\"human_gut\""):
             #   pos -= 1
             pos = pos2+1
             while (pos2 > 0):
                 if (self.contents[i][pos2] == "\"NA\"" or self.contents[i][pos2].endswith('unclassified\"') or
                      self.contents[i][pos2].startswith('\"uncultured') or self.contents[i][pos2] == "\"metagenome\"" or self.contents[i][pos2] == "\"gut_metagenome\"" or self.contents[i][pos2] == "\"unidentified\"" or self.contents[i][pos2] == "\"human_gut\""):
                     pos = pos2
                 pos2 -= 1
             if (pos == 0):
                 for j in range(0, self.N-1):
                    self.contents[i][j] = '\"Unclassified\"'
             elif (pos == 8 and not self.contents[i][7].startswith("\""+unquote(self.contents[i][6]))):
                 self.contents[i][7] = '\"' + unquote(self.contents[i][6])+" "+unquote(self.contents[i][7]) + '\"'
             else:
              for j in range(pos, self.N):
                 self.contents[i][j] = '\"' + unquote(self.contents[i][pos-1])+"("+LEVELS[pos-1]+")" + '\"'

    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.firstline)
       for i in range(len(self.contents)):
         for j in range(self.N):
          outfile.write(self.contents[i][j])
          if (j < self.N-1):
             outfile.write(',')
          else:
             outfile.write('\n')

