module Floyd
       where

import Control.Applicative ( (<$>) )
import Control.Exception   ( assert )
import Control.Monad       ( forM_, when )
import Data.Array.IArray
import Data.Array.MArray
import Data.Array.ST
import Data.Maybe          ( fromMaybe )

infty :: Int
infty = 10^6

floydAlgorithm :: Array (Int, Int) (Maybe Int) -> Array (Int, Int) (Maybe Int)
floydAlgorithm iarr = assert precondition oarr
  where
    bnds         = bounds iarr
    b1           = fst bnds
    b2           = snd bnds
    precondition = (fst b1 == snd b1) && (fst b1 == 1)
                   && (fst b2 == snd b2)

    n = fst b2

    oarr = runSTArray $ do
      marr <- thaw iarr
      forM_ [1..n] $ \k ->
        forM_ [1..n] $ \i ->
          forM_ [1..n] $ \j -> do
            marrIK <- fromMaybe infty <$> readArray marr (i,k)
            marrKJ <- fromMaybe infty <$> readArray marr (k,j)
            marrIJ <- fromMaybe infty <$> readArray marr (i,j)
            when (marrIK + marrKJ < marrIJ) $
              writeArray marr (i,j) (Just $ marrIK + marrKJ)
      return marr

main :: IO ()
main = do let graph = [((1,1), 0), ((2,2), 0), ((3,3), 0),
                       ((4,4), 0), ((5,5), 0), ((6,6), 0),
                       ((2,1), 1), ((2,3), 1), ((3,4), 1),
                       ((3,6), 1), ((4,3), 1), ((5,4), 1),
                       ((5,2), 1), ((6,1), 1)]
              arr = runSTArray $ do
                marr <- newArray ((1,1),(6,6)) Nothing
                forM_ graph $ \(i,v) ->
                  writeArray marr i (Just v)
                return marr
          print . foldr onlyJust [] . assocs . floydAlgorithm $ arr
            where
              onlyJust (i, Just v)  xs = (i,v):xs
              onlyJust (_, Nothing) xs = xs
