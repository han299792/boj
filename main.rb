grid = []
9.times { grid << gets.split.map(&:to_i) }

max_val = -1
row = col = 0

9.times do |i|
  9.times do |j|
    if grid[i][j] > max_val
      max_val = grid[i][j]
      row = i + 1
      col = j + 1
    end
  end
end

puts max_val
puts "#{row} #{col}"
