# Tower of Hanoi or Tower of Brahma
# >>>------------------------------>

def moveTower(n, source, dest, temp):
  """
  Algorithm: move n-disk tower from source to destination via resting place
  -- move n-1 disk tower from source to resting place
  -- move 1 disk tower from source to destination
  -- move n-1 disk tower from resting place to destination
  """
