import MainReader
import DataParser
import BoxOrganizer
import sys
import Speak

def main():
    # works on understanding cmd line options
    programRun = MainReader.MainReader(sys.argv)
    path = programRun.getPath()
        # gathering list indecies 
    ignorableList = programRun.getIgnorable()
    searchableList = programRun.getSearchable()

    # reads given csv, and processeses cmd line -i(ignore column) option
    parsedData = DataParser.DataParser(path, ignorableList)

    boxList = []
    # processes cmd line -s(searchable columns) option
    for i in range(len(searchableList)):
        int_search_index = int(searchableList[i])

        # to account for deleted columns
        for j in range(len(ignorableList)):
            i_temp = int(ignorableList[j])
            if i_temp < int_search_index:
                int_search_index = int_search_index -1

        box = BoxOrganizer.BoxOrganizer(parsedData.globalList[int_search_index-1]) # -1 to account for 0 index
        print(box.searchList("Am"))
        #print(int_search_index-1)
        boxList.append(box)
        
   # for i in range(len(parsedData.globalList)):
      #  print(parsedData.globalList[i][0])

if __name__ == "__main__":
    main()