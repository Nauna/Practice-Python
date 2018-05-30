
class  BoxOrganizer:
    def __init__(self, unsortedList):
        if unsortedList != "none":
            self.unsortedList = unsortedList
        else:
            print("box list error")
        self.createReference_sort()

    def createReference_sort(self):
        self.sortedList = sorted(enumerate(self.unsortedList), key=lambda x: x[1])
        
        
    def searchList(self, key = ""):
        if key == "":
            return self.sortedList
        else:
            string_size = len(key)
            portioned_list = self.sortedList
            for i in range(string_size):
                #setting variables
                char_key = key[i] # sequential need to compare input key string
                list_size = len(portioned_list) # size of list we need to narrow down
                while_index = 0 # counting variable
                first = True
                last = False
                index_start = 0
                index_end = 0

                # going through our main list, trying to narrow down list based off of key input
                while (while_index < list_size):
                    # checking if len(list var) is within key size - mainly a check for empty entries in column
                    if ((len(portioned_list[while_index][1])-1) > i):
                        #if main list(portioned_list) value while_index, has the same position char as key(char_key)
                        if portioned_list[while_index][1][i] == char_key:
                            # then mark the first occurance of a match
                            if first:
                                index_start = while_index
                                first = False
                                last = True
                        else:
                            # mark the last occurance of a match, notice this value is the index of the match after the last match
                            if last:
                                index_end = while_index
                                break #to end loop: we got what we wanted {index_start, index_end}
                    #increment for next loop
                    while_index = while_index + 1
                # possible that index_end is not set because entire list is included
                if last:
                    index_end = while_index-1
                # if error and we didn't get what we wanted then ...
                if index_end <= index_start:
                    #print("No matches to key = %s" % char_key)
                    #print("index_end = %s , index_start = %s" % (index_end, index_start))
                    return []
                # break down list based on discovered indicies
                portioned_list = portioned_list[index_start:index_end]

        return portioned_list


    def referenceList(self,key):
        indexStart = 0
        indexEnd = 0