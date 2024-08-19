# Birthday guessing based on the binary search algo

def ask_question_and_grab_input(text):
    print(text)
    # assuming that a user can do so correctly (strong assumption, but let's keep it simple)
    if input().lower()[0] == 't':
        return True
    else:
        return False 

def binary_search_w_asking(arr, month='', count=5):
    low = arr[0]
    high = arr[-1]
    mid = 0
    count = count
 
    while high - low > 1:

        mid = (high + low) // 2

        lower_than_mid = ask_question_and_grab_input(f"#{count} Czy masz urodziny {mid} {month} lub wczesniej? Odpowiedz tak albo nie.")

        # If x is smaller, ignore right half
        if lower_than_mid:
            high = mid

        # If x is greater, ignore left half
        else:
            low = mid + 1

        count+=1
    
    if high - low == 1:
        last_q = ask_question_and_grab_input(f"Ostatnie pytanie, dla upewnienia - czy masz urodziny dokladnie {high} {month}? Odpowiedz tak albo nie.")

        if last_q:
            day = high
        else:
            day = low

    else:
        day = high
    
    return day 
 
def zgadnij_urodziny(month=None):
    print("Zgadne Twoja date urodzenia w dokladnie 9 krokach!\nZaczynajmy!")

    def month_guess():
                
        # Month 1st question
        warm_seasons = ask_question_and_grab_input("#1 Czy Twoje urodziny sa w ciepla pore roku (wiosna-lato)? Wpisz tak albo nie")

        # Month 2nd question
        if warm_seasons: # warm seasons
            season = ask_question_and_grab_input("#2 Czy Twoje urodziny sa wiosna (marzec/kwiecien/maj)? Wpisz tak albo nie")
            
            # Month 3rd question - warm seasons
            if season: # spring
                mar = ask_question_and_grab_input("#3 Czy Twoje urodziny sa w marcu? Wpisz tak albo nie")
                
                # Month 4th question - March vs other
                if mar:
                    month = 'marca'

                else: # Month 5th question (optional)
                    april = ask_question_and_grab_input("#4 Czy Twoje urodziny sa w kwietniu? Wpisz tak albo nie")

                    if april:
                        month = 'kwietnia'
                    else:
                        print('No tak, masz urodziny w maju!')
                        month = 'maja'

            else: # summer
                june = ask_question_and_grab_input("#3 Czy Twoje urodziny sa w czerwcu? Wpisz tak albo nie")

                # Month 4th question - June vs other
                if june:
                    month = 'czerwca'

                else: # Month 5th question (optional)
                    july = ask_question_and_grab_input("#4 Czy Twoje urodziny sa w lipcu? Wpisz tak albo nie")

                    if july:
                        month = 'lipca'
                    else:
                        print('No tak, masz urodziny w sierpniu!')
                        month = 'sierpnia'

        else: # cold seasons
            season = ask_question_and_grab_input("#2 Czy Twoje urodziny sa jesienia (wrzesien/pazdziernik/listopad)? Wpisz tak albo nie")

            # Month 3rd question - cold seasons
            if season: # autumn
                sept = ask_question_and_grab_input("#3 Czy Twoje urodziny sa we wrzesniu? Wpisz tak albo nie")

                # Month 4th question - Sept vs other
                if sept:
                    month = 'wrzesnia'

                else: # Month 5th question (optional)
                    nov = ask_question_and_grab_input("#4 Czy Twoje urodziny sa w pazdzierniku? Wpisz tak albo nie")

                    if nov:
                        month = 'pazdziernika'
                    else:
                        print('No tak, masz urodziny w listopadzie!')
                        month = 'listopada'

            else: # winter
                dec = ask_question_and_grab_input("#3 Czy Twoje urodziny sa w grudniu? Wpisz tak albo nie")

                # Month 4th question - June vs other
                if dec:
                    month = 'grudnia'

                else: # Month 5th question (optional)
                    jan = ask_question_and_grab_input("#4 Czy Twoje urodziny sa w styczniu? Wpisz tak albo nie")

                    if jan:
                        month = 'stycznia'
                    else:
                        print('No tak, masz urodziny w lutym!')
                        month = 'lutego'

        return month
    
    def day_guess(month):
        arr = [i for i in range(1,32)] # 1..31
        return binary_search_w_asking(arr, month)

    if not month:
        month = month_guess()

    day = day_guess(month)

    print(f"Masz urodziny {day} {month}!")

if __name__ == "__main__":
    zgadnij_urodziny()
