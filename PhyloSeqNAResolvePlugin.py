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
          if (len(self.contents[i]) > 7 and self.contents[i][7] != "\"NA\"" and (not self.contents[i][7].endswith('unclassified\"')) and (not self.contents[i][7].startswith('\"uncultured'))):
             self.contents[i][7] = '\"' + unquote(self.contents[i][6])+" "+unquote(self.contents[i][7]) + '\"'
          else:  # Species is NA.  Go back to the first position that is not
             pos = self.N-1
             while (self.contents[i][pos] == "\"NA\"" or self.contents[i][pos].endswith('unclassified\"') or
                      self.contents[i][pos].startswith('\"uncultured')):
                pos -= 1
             # pos is at first non-NA spot
             if (pos == 0):
                 for j in range(0, self.N-1):
                    self.contents[i][j] = '\"Unclassified\"'
             else:
              for j in range(pos+1, self.N):
                 self.contents[i][j] = '\"' + unquote(self.contents[i][pos])+"("+LEVELS[pos]+")" + '\"'

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

