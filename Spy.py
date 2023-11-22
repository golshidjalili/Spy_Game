def encrypt(word, n):
    german_letters = 'abcdefghijklmnopqrstuvwxyzäöüß'
    word_list = []
    for letter in word:
        word_list.append(letter)
    word_encrypted = ''
    for letter in word_list:
        letter_index = german_letters.find(letter)
        letter_encrypted_index = (letter_index + n) % 30
        word_encrypted += german_letters[letter_encrypted_index]
    return word_encrypted


def decrypt(word, n):
    german_letters = 'abcdefghijklmnopqrstuvwxyzäöüß'
    word_list = []
    for letter in word:
        word_list.append(letter)
    word_decrypted = ''
    for letter in word_list:
        letter_index = german_letters.find(letter)
        letter_decrypted_index = (letter_index - n) % 30
        word_decrypted += german_letters[letter_decrypted_index]
    return word_decrypted


def spy(letter, spy_word):
    letter_without_punc = letter.replace('.', '').replace(',', '')
    letter_without_punc_list = letter_without_punc.split(' ')
    n_to_decrypt_with = 0
    is_n_found = False
    for word in letter_without_punc_list:
        for n in range(30):
            if decrypt(word, n) == spy_word:
                n_to_decrypt_with = n
                is_n_found = True
                break
        if is_n_found:
            break
    letter_decrypted = []
    for word in letter_without_punc_list:
        letter_decrypted.append(decrypt(word, n_to_decrypt_with))
    decrypted_letter = ' '.join(letter_decrypted)
    print(decrypted_letter)

letter = 'nä qrä sluara däq arvpubxnäiyra. orvz eraynmrä qrdcbpuynäqb qnäxrä qvr uraiötvä eöä fväqböa däq vpu vuärä ndsavpucvt sla qvr taömr tndcsardäqbpunsc, qvr bvr däb trfjuac unorä däq sla qvr evryrä zktyvpuxrvcrä, qnb id brurä, fnb sla qnb föuy qra bpunssräqrä qrdcbpurä trcnä fvaq. fva äruzrä rvärä cvrsrä rväqadpx eöä däbrara arvbr qdapu qrdcbpuynäq zvc däq fraqrä ävr eratrmrä, zvc frypura ndszraxbnzxrvc fva eöä vuarä orndscanträ dztrorä föaqrä bväq, däq rvär fvr uraiyvpur ndsäruzrä fva loranyy trsdäqrä unorä. orböäqrab qnäxrä fva vuärä sla qvr bpukärä bcdäqrä, qvr fva zvc vuärä nds qrz öorabnyiorat eraoanpuc unorä.'
spy_word = 'obersalzberg'

spy(letter, spy_word)