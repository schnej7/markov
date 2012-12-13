import random
from markov import markov
import sys
import csv
import ast
import py_compile

depth = 5

def clean( word ):
    bad_chars = []
    for letter in word.lower():
        if (letter > 'z' or letter < 'a') and (letter != '.' and letter != '?' and letter != '!') :
            bad_chars.append( letter )

    for char in bad_chars:
        word = word.replace( char, '' )
    return word.lower()

def dump( filename ):
    import cPickle
    f = open( filename )
    Markov = markov()
    prev_word = [ '' ]
    line = f.readline()
    all_words = set()
    lines = 0
    while True:
        lines += 1
        if lines % 10 == 0:
            sys.stdout.write( '\r%d' % lines )
            sys.stdout.flush()
        line = line.replace( '.', ' .')
        line = line.replace( '?', ' ?')
        line = line.replace( '!', ' !')
        prev_word = ['']
        for word in line.split(' '):
            word = clean(word)
            if len( word ) == 0:
                continue
            all_words.add( word )
            for i in range( depth ):
                if i > len( prev_word ):
                    break;
                Markov.record( ' '.join(prev_word[-i:]).lower(), word )
            prev_word.append( word )
            if len( prev_word ) > depth:
                prev_word.pop(0)

        line = f.readline()
        if len( line ) == 0:
            f.close()
            break

    print ''
    all_words = list( all_words )

    cPickle.dump( Markov, open( '.m_' + filename + '.dmp', "wb" ) )
    cPickle.dump( all_words, open( '.w_' + filename + '.dmp', "wb" ) )

    load( Markov, all_words, None )

def load( a_Markov, a_all_words, filename ):
    if a_Markov == None:
        import cPickle
        Markov = markov()
        Markov = cPickle.load( open( ".m_" + filename + '.dmp', "rb" ) )
        all_words = cPickle.load( open( ".w_" + filename + '.dmp', "rb" ) )
    else:
        Markov = a_Markov
        all_words = a_all_words
    new_words = [ '' ]

    print "total:", len( all_words )
    new_words.append( Markov.predict( ' '.join(new_words[ -1:]).lower() ) )
    j = 0
    while j < 500 or ( next_word != '.' and next_word != '!' and next_word != '?' ):
        j += 1
        next_word = None
        i = depth;
        while next_word == None and i > 0:
            next_word = Markov.predict( ' '.join(new_words[ -i:]).lower() )
            i -= 1
        if next_word == None and new_words[-1:][0] in ['.','?','!']:
            next_word = '\n\n' + Markov.predict( '' )
        if next_word == None:
            next_word = Markov.predict( '' )
        new_words.append( next_word )

    output = ' '.join(new_words)
    output = output.replace( ' .', '.' )
    output = output.replace( ' ?', '?' )
    output = output.replace( ' !', '!' )
    print output

if __name__ == '__main__':
    if len( sys.argv ) < 2:
        print 'No file selected'
        sys.exit()
    try:
        #If the processed data exists...
        f = open('.m_' + sys.argv[1] + '.dmp')
        f.close()
        f = open('.w_' + sys.argv[1] + '.dmp')
        f.close()
        load( None, None, sys.argv[1] )
    except IOError as e:
        try:
            f = open(sys.argv[1])
            f.close()
            print 'Oh dear, processing file...'
            dump( sys.argv[1] )
        except IOError as ee:
            print 'The file ' + sys.argv[1] + ' does not exist...'
