from markov import markov
import cPickle
import sys

depth = 5
punc = [ '.', '?', '!' ]

def clean( word ):
    bad_chars = []
    for letter in word.lower():
        if (letter > 'z' or letter < 'a') and letter not in punc:
            bad_chars.append( letter )

    for char in bad_chars:
        word = word.replace( char, '' )
    return word.lower()


def load( filename ):
    Markov = markov()
    Markov = cPickle.load( open( ".m_" + filename + '.dmp', "rb" ) )
    return Markov

def save( filename, Markov ):
    cPickle.dump( Markov, open( '.m_' + filename + '.save.dmp', "wb" ) )

def play( filename, Markov ):
    Words = [ '' ]
    while( True ):
        if len( Words ) > depth:
            Words.pop(0)
        next_word = None
        i = min( [depth, len( Words )] )
        while next_word == None and i > 0:
            next_word = Markov.predict( ' '.join(Words[ -i:]).lower() )
            i -= 1
        if next_word == None:
            next_word = Markov.predict( '' )
        Words.append( next_word )
        sys.stdout.write( '%s ' % next_word )
        sys.stdout.flush()

        for word in raw_input().split(' '):
            if word == '': break
            next_word = clean( word )
            if next_word == '!!!!!':
                save( filename, Markov )
                return

            i = min( [depth, len( Words )] )
            while next_word == None and i > 0:
                next_word = Markov.record( ' '.join(Words[ -i:]).lower(), next_word )
                i -= 1
            Words.append( next_word )

def main():
    if len( sys.argv ) < 2:
        print 'Not enough args'
        return
    try:
        f = open( '.m_' + sys.argv[1] + '.dmp' )
        f.close()
    except IOError as e:
        print 'No file data exists...'
        return

    Markov = load( sys.argv[1] )

    play( sys.argv[1], Markov )


if __name__ == '__main__':
    main()
