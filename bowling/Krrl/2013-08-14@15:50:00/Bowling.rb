def strike (currentgame, currentindex)
  framescore = 10
  secondball = currentgame[currentindex+1]
  thirdball = currentgame[currentindex+2]
  if secondball == 'X' and thirdball == 'X'
    framescore += 20
  elsif secondball != 'X' and thirdball == '/'
    framescore += 10
  elsif secondball == 'X' and thirdball != 'X'
    framescore += 10
    framescore += thirdball.to_i
  else
    framescore += secondball.to_i
    framescore += thirdball.to_i
  end
  return framescore
end

def spare (currentgame, currentindex)
  framescore = 10
  secondball = currentgame[currentindex+2]
  if secondball == 'X'
    framescore += 10
  else
    framescore += secondball.to_i
  end
  return framescore
end

def scoring(game)
  i = 0
  frame = 1
  totalscore = 0
  while frame <= 10
    if game[i] == 'X'
      totalscore += strike(game, i)
      i += 1
      frame += 1
    elsif game[i+1] == '/'
      totalscore += spare(game, i)
      i += 2
      frame += 1
    else
      totalscore += game[i].to_i
      totalscore += game[i+1].to_i
      i += 2
      frame += 1
    end
  end
  return totalscore
end

if ARGV.length != 1
  puts "Usage: bowling.rb <inputfile>"
  abort()
end

lines = IO.readlines ARGV[0]

while lines[-1] == ""
  lines.delete(lines[-1])
end

lines.each do |line|
  game = []
  line.each_char do |ball|
    if ball == " "
      next
    else
      game.push(ball)
    end
  end
  puts scoring(game)
end