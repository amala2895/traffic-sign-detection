# traffic-sign-detection
Traffic Sign Detection using CNN


# Convolution Training Network
Layer 1 CNN
Input 32 x 32 x 3 Kernel 5 x 5 Padding = 2
Output 32 x 32 x 32

Layer 2 Max Pool (2,2)
Output 16 x 16 x 32

Layer 3 ReLu
Layer 4 CNN
Input 16 x 16 x 32 Kernel 5 x 5 Padding = 2
Output 16 x 16 x 64 Dropout with p =0.1

Layer 5 Max Pool (2,2)
Output 8 x 8 x 64

Layer 6 ReLu
Layer 7 CNN
Input 8 x 8 x 64 Kernel 5 x 5 Padding = 2
Output 8x 8 x 128 Dropout with p =0.3

Layer 8 Max Pool (2,2)
Output 4 x 4 x 124

Layer 9 ReLu

Flatten to 128 x 4 x 4

Layer 10 Fully connected
Input = 2048 Output = 128

Layer 11 ReLu
Dropout

Layer 12 Fully connected
Input = 128 Output = 43
