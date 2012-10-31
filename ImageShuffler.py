from random import shuffle
import time
import sys


#main function to call for image processing
def shuffleImage( inputImage, outputImage, shuffleStart = 150, shuffleLen = 1, shuffleGap = 20, shuffleCount = 80, randomize = False, descString = None ):
    lines = openFile( inputImage )
    finalLines = doShuffle( lines, shuffleStart, shuffleLen, shuffleGap, shuffleCount, randomize )
    storeImage( outputImage + ".jpg", finalLines ) 

    #write description file along with the image
    if descString is None: 
        descString = "shuffleStart: " + str( shuffleStart ) + ", shuffleLen: " + str( shuffleLen ) + ", shuffleGap: " + str( shuffleGap ) + ", shuffleCount: " + str( shuffleCount ) + ", randomize: " + str( randomize )
    writeDescFile( outputImage + ".txt", descString )

#function to open file with specified url
def openFile( fileUrl ):
    try:
        f = open( str( fileUrl ), "r")
        try:
            lines = f.readlines()
        finally:
            f.close()
    except IOError:
        pass

    return lines;

#core function processing end shuffling lines of image
def doShuffle( lines, shuffleStart, shuffleLen, shuffleGap, shuffleCount, randomize ):

    #print to console what is the script is doing
    print( "doShuffle: " + str( shuffleStart ) + ", shuffleLen: " + str( shuffleLen ) + ", shuffleGap: " + str( shuffleGap ) + ", shuffleCount: " + str( shuffleCount ) + ", randomize: " + str( randomize ) )
    
    #put lines into iterator
    linesIterator = iter( lines )
   
    #numOfLines in image
    numLines = len( lines )

    #setup arrays
    headerLines = []
    rowLines = []
    imageLines = []
    restLines = []

    #index of current line
    nowLine = 0

    #loop through header lines
    for item in range( 0, shuffleStart):
       	#add header lines without alteration to header array
        headerLines.append( linesIterator.next() )

    #put all lines to final array with all lines
    finalLines = headerLines

    #update index to first modifying lines
    nowLine = shuffleStart

    for item in range( 0, shuffleCount ):
        
        #loop through image lines
        start = nowLine
        end = nowLine + shuffleLen

        cuttedLines = []

        #loop through all lines that are supposed to be cut and pasted else
        for item in range( start, end):
            cuttedLines.append( linesIterator.next() )
       
        #if randomize flag set to True, cutted lines will be shuffled among themselves    
        if( randomize ): 
            shuffle( cuttedLines )

        rowLines = []

        #iterater through gap to get to point
        for item in range( end, end + shuffleGap ):
            rowLines.append( linesIterator.next() )
        
        #put unaltered lines
        finalLines += rowLines

        #paste cutted lines
        finalLines += cuttedLines

        #update nowLine index
        nowLine = end + shuffleGap
        
    #put the rest of lines to complete image    
    for item in range( nowLine, numLines ):
        restLines.append( linesIterator.next() )
   
    finalLines += restLines

    return finalLines

#save image to specify path
def storeImage( newFileUrl, lines ):

    try:
        f = open( newFileUrl, "w")
        try:
            #f.write( string ) # Write a string to a file
            f.writelines( lines ) # Write a sequence of strings to a file
        finally:
            f.close()
    except IOError:
        pass


#write description file
def writeDescFile( fileUrl, string ):
    try:
        f = open( fileUrl, "w")
        try:
            f.write( string ) # Write a string to a file
        finally:
            f.close()
    except IOError:
        pass


if __name__ == "__main__":
    
    #read and set params from users input
    argsLen = len( sys.argv )

    #numOfLines that will be left intact at the beginnig of the jpeg file
    if argsLen > 2 :
        shuffleStart = int( sys.argv[ 2 ] )
    else :
        shuffleStart = 150

    #shuffleLen = number of images lines that will be taken out of context and paste somewhere else
    if argsLen > 3 :
        shuffleLen = int( sys.argv[ 3 ] )
    else :
        shuffleLen = 10

    if argsLen > 4 :
        shuffleGap = int( sys.argv[ 4 ] )
    else :
        shuffleGap = 1

    #shuffleCount = number of times lines will be taken out of context and paste somewhere    
    if argsLen > 5 :
        shuffleCount = int( sys.argv[ 5 ] )
    else :
        shuffleCount = 10

    if argsLen > 6 :
        randomize = int( sys.argv[ 6 ] )
    else :
        randomize = False
    
    #read bytes from inputed image url
    imageInput = sys.argv[ 1 ]

    #create timestamp for image name
    timeStamp = str( time.time() )
    #create image output path
    imageOutput = imageInput + "-" + timeStamp

    #create string description that will be put into accompying text file
    descString = "shuffleStart: " + str( shuffleStart ) + ", shuffleLen: " + str( shuffleLen ) + ", shuffleGap: " + str( shuffleGap ) + ", shuffleCount: " + str( shuffleCount ) + ", randomize: " + str( randomize )
    
    #do the image processing
    shuffleImage( imageInput, imageOutput, shuffleStart, shuffleLen, shuffleGap, shuffleCount, randomize, descString ) 

