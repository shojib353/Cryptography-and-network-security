#include <iostream>
using namespace std;


string caesar(string text,int key){
    string result="";

    for(int i=0;i<text.length();i++){
            char x=text[i];
         if (text[i] >= 'a' && text[i] <= 'z'){

        x=(((text[i]-'a')+key)%26)+'a';
    }
    else{

        x=(((text[i]-'A')+key)%26)+'A';
    }
    result+=x;


    }
    return result;

}

string caesarDecrypt(string text,int key){
    string result="";
    char x;
    for(int i=0;i<text.length();i++){
         if (text[i] >= 'a' && text[i] <= 'z'){
        x=((text[i]-'a')-key)%26+'a';
    }
    else{
        x=((text[i]-'A')-key)%26+'A';
    }
    result+=x;


    }
    return result;

}


string encrypt(string plaintext, string key) {
    string ciphertext = "";

        for (int i = 0; i < plaintext.length(); i++) {
        if (plaintext[i] >= 'A' && plaintext[i] <= 'Z'){
        ciphertext += key[plaintext[i] - 'A'];
        }

        //step 1:key[S-'A'];
        //step 2:key[18]=E

        else{
            ciphertext += key[plaintext[i] - 'a'];
        }


    }

    return ciphertext;
}


string decrypt(string ciphertext, string key) {
    string decrypted = "";
    for (int i = 0; i < ciphertext.length(); i++) {

        for (int j = 0; j < 26; j++) {
            if (key[j] == ciphertext[i]) {
                decrypted += char('A' + j);
                //char(83)=S;
                break;
            }
        }
    }
    return decrypted;
}

int main() {
    string plaintext = "SHoiIB";
    string key = "MNBVCXZLKJHGFDSAQWERTYUIOP";


    string caesarencrypted = caesar("SHOJIB", 3);
    cout << "caesar encrypted: " << caesarencrypted << endl;

    string caesardecrypted = caesarDecrypt(caesarencrypted, 3);
    cout << "Caesar Decrypted: " << caesardecrypted << endl;

    string ciphertext = encrypt(plaintext, key);
    cout << "Mono AlPhabetic Encrypted: " << ciphertext << endl;

    string decrypted = decrypt(ciphertext, key);
    cout << "Mono AlPhabetic Decrypted: " << decrypted << endl;


    return 0;
}
