status = True

while status:

    sentence = input('Send me a sentence and I check it for you : ')

    words = sentence.split()

    i=0
    longest=0

    while ( i < len(words) ):

        if ( len(words[i]) > longest ):
            longest = len(words[i])
            longestWord = words[i]
        
        i += 1

    print('Length of longest word in your sentece is : ', longest, ', and the word is : ', longestWord)

    again = input('Do you want to try again ? (Yes or No) : ').title().replace(" ","")

    if again == 'Yes':
        print('OK! Lets try again')

    elif again == 'No':
        print("Bye then...")
        status = False

    else:
        print('Funny it is not a Yes or No but I accept that as a big YYYYEEEESSS')