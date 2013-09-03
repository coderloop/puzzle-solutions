#!/usr/bin/ruby
# write your solution to spiesstory

ALPHABET_LENGTH = 26
message = File.new(ARGV.first, 'r')
cipher = message.gets.chop
cipher = cipher.to_i % ALPHABET_LENGTH
@dec_map = {}
def decipher_char(cipher, char)
  dec_char = char
  if (char.chr =~ /[A-Z]/)
    dec_char -= cipher
    dec_char += ALPHABET_LENGTH if (dec_char < 65)
  elsif char.chr =~ /[a-z]/
    dec_char -= cipher
    dec_char += ALPHABET_LENGTH if (dec_char < 97)
  end
  @dec_map[char] = dec_char
end
decripted = ""
message.each_byte {|c| decripted << (@dec_map[c] || decipher_char(cipher, c)) }
print decripted
