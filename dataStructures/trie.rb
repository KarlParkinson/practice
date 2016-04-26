class Trie

  def initialize
    @count = 0
    @root = TrieNode.new
    @alphabet = ("a".."z").to_a
  end

  def insert(key)
    key = key.downcase
    pCrawl = @root
    @count += 1
    key.each_char do |c|
      ind = @alphabet.index(c)
      if (pCrawl.children[ind].nil?)
        pCrawl.children[ind] = TrieNode.new
      end
      pCrawl = pCrawl.children[ind]
    end
    pCrawl.value = @count
  end

  def search(key)
    key = key.downcase
    pCrawl = @root
    key.each_char do |c|
      ind = @alphabet.index(c)
      if (pCrawl.children[ind].nil?)
        return false
      end
      pCrawl = pCrawl.children[ind]
    end
    return pCrawl
  end

end

class TrieNode

  attr_accessor :value, :children

  def initialize
    self.value = 0
    self.children = [nil]*26
  end

end
