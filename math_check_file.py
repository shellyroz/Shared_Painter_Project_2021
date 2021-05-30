sent = '''sent: 
(626, 173)
sent: 
(627, 172)
sent: 
(627, 171)
sent: 
(629, 170)
sent: 
(630, 169)
sent: 
(630, 168)
sent: 
(631, 167)
sent: 
(634, 166)
sent: 
(638, 165)
sent: 
(639, 165)
sent: 
(640, 164)
sent: 
(641, 164)
sent: 
(642, 164)
sent: 
(646, 168)
sent: 
(646, 170)
sent: 
(646, 171)
sent: 
(646, 172)
sent: 
(646, 177)
sent: 
(646, 178)
sent: 
(646, 180)
sent: 
(646, 182)
sent: 
(645, 183)
sent: 
(645, 184)
sent: 
(640, 188)
sent: 
(639, 189)
sent: 
(639, 190)
sent: 
(638, 191)
sent: 
(634, 198)
sent: 
(633, 199)
sent: 
(630, 203)
sent: 
(629, 205)
sent: 
(629, 207)
sent: 
(628, 208)
sent: 
(627, 209)
sent: 
(627, 211)
sent: 
(626, 213)
sent: 
(625, 215)
sent: 
(625, 217)
sent: 
(624, 219)
sent: 
(624, 221)
sent: 
(623, 221)
sent: 
(623, 220)
sent: 
(622, 219)
sent: 
(620, 215)
sent: 
(619, 213)
sent: 
(618, 212)
sent: 
(617, 210)
sent: 
(616, 207)
sent: 
(615, 205)
sent: 
(614, 204)
sent: 
(614, 203)
sent: 
(614, 202)
sent: 
(613, 201)
sent: 
(611, 195)
sent: 
(611, 194)
sent: 
(610, 191)
sent: 
(610, 190)
sent: 
(609, 189)
sent: 
(609, 186)
sent: 
(608, 185)
sent: 
(608, 182)
sent: 
(608, 178)
sent: 
(608, 177)
sent: 
(608, 175)
sent: 
(608, 174)
sent: 
(608, 171)
sent: 
(608, 169)
sent: 
(609, 168)
sent: 
(609, 167)
sent: 
(609, 166)
sent: 
(610, 165)
sent: 
(612, 164)
sent: 
(613, 164)
sent: 
(614, 164)
sent: 
(618, 164)
sent: 
(619, 164)
sent: 
(619, 165)
sent: 
(619, 166)
sent: 
(619, 167)
sent: 
(620, 167)
sent: 
(620, 168)
sent: 
(620, 169)
sent: 
(620, 170)
sent: 
(621, 171)
sent: 
(621, 173)
sent: 
(621, 174)
sent: 
(622, 174)
sent: 
(623, 174)'''

sent = sent.replace('\n', '')
sent = sent.replace(' ', '')
sent = sent.replace('sent:', '')
sent = sent.replace(')', '), ')
lst1 = list(sent.split(", "))


paint = '''received: 
(626, 173)
color: 
(626, 173)
color: 
(626, 174)
color: 
(626, 175)
color: 
(627, 173)
color: 
(627, 174)
color: 
(627, 175)
color: 
(628, 173)
color: 
(628, 174)
color: 
(628, 175)
received: 
(627, 172)
color: 
(627, 172)
color: 
(627, 173)
color: 
(627, 174)
color: 
(628, 172)
color: 
(628, 173)
color: 
(628, 174)
color: 
(629, 172)
color: 
(629, 173)
color: 
(629, 174)
received: 
(627, 171)
color: 
(627, 171)
color: 
(627, 172)
color: 
(627, 173)
color: 
(628, 171)
color: 
(628, 172)
color: 
(628, 173)
color: 
(629, 171)
color: 
(629, 172)
color: 
(629, 173)
received: 
(629, 170)
color: 
(629, 170)
color: 
(629, 171)
color: 
(629, 172)
color: 
(630, 170)
color: 
(630, 171)
color: 
(630, 172)
color: 
(631, 170)
color: 
(631, 171)
color: 
(631, 172)
received: 
(630, 169)
color: 
(630, 169)
color: 
(630, 170)
color: 
(630, 171)
color: 
(631, 169)
color: 
(631, 170)
color: 
(631, 171)
color: 
(632, 169)
color: 
(632, 170)
color: 
(632, 171)
received: 
(630, 168)
color: 
(630, 168)
color: 
(630, 169)
color: 
(630, 170)
color: 
(631, 168)
color: 
(631, 169)
color: 
(631, 170)
color: 
(632, 168)
color: 
(632, 169)
color: 
(632, 170)
received: 
(631, 167)
color: 
(631, 167)
color: 
(631, 168)
color: 
(631, 169)
color: 
(632, 167)
color: 
(632, 168)
color: 
(632, 169)
color: 
(633, 167)
color: 
(633, 168)
color: 
(633, 169)
received: 
(634, 166)
color: 
(634, 166)
color: 
(634, 167)
color: 
(634, 168)
color: 
(635, 166)
color: 
(635, 167)
color: 
(635, 168)
color: 
(636, 166)
color: 
(636, 167)
color: 
(636, 168)
received: 
(638, 165)
color: 
(638, 165)
color: 
(638, 166)
color: 
(638, 167)
color: 
(639, 165)
color: 
(639, 166)
color: 
(639, 167)
color: 
(640, 165)
color: 
(640, 166)
color: 
(640, 167)
received: 
(639, 165)
color: 
(639, 165)
color: 
(639, 166)
color: 
(639, 167)
color: 
(640, 165)
color: 
(640, 166)
color: 
(640, 167)
color: 
(641, 165)
color: 
(641, 166)
color: 
(641, 167)
received: 
(640, 164)
color: 
(640, 164)
color: 
(640, 165)
color: 
(640, 166)
color: 
(641, 164)
color: 
(641, 165)
color: 
(641, 166)
color: 
(642, 164)
color: 
(642, 165)
color: 
(642, 166)
received: 
(641, 164)
color: 
(641, 164)
color: 
(641, 165)
color: 
(641, 166)
color: 
(642, 164)
color: 
(642, 165)
color: 
(642, 166)
color: 
(643, 164)
color: 
(643, 165)
color: 
(643, 166)
received: 
(642, 164)
color: 
(642, 164)
color: 
(642, 165)
color: 
(642, 166)
color: 
(643, 164)
color: 
(643, 165)
color: 
(643, 166)
color: 
(644, 164)
color: 
(644, 165)
color: 
(644, 166)
received: 
(646, 168)
color: 
(646, 168)
color: 
(646, 169)
color: 
(646, 170)
color: 
(647, 168)
color: 
(647, 169)
color: 
(647, 170)
color: 
(648, 168)
color: 
(648, 169)
color: 
(648, 170)
received: 
(646, 170)
color: 
(646, 170)
color: 
(646, 171)
color: 
(646, 172)
color: 
(647, 170)
color: 
(647, 171)
color: 
(647, 172)
color: 
(648, 170)
color: 
(648, 171)
color: 
(648, 172)
received: 
(646, 171)
color: 
(646, 171)
color: 
(646, 172)
color: 
(646, 173)
color: 
(647, 171)
color: 
(647, 172)
color: 
(647, 173)
color: 
(648, 171)
color: 
(648, 172)
color: 
(648, 173)
received: 
(646, 172)
color: 
(646, 172)
color: 
(646, 173)
color: 
(646, 174)
color: 
(647, 172)
color: 
(647, 173)
color: 
(647, 174)
color: 
(648, 172)
color: 
(648, 173)
color: 
(648, 174)
received: 
(646, 177)
color: 
(646, 177)
color: 
(646, 178)
color: 
(646, 179)
color: 
(647, 177)
color: 
(647, 178)
color: 
(647, 179)
color: 
(648, 177)
color: 
(648, 178)
color: 
(648, 179)
received: 
(646, 178)
color: 
(646, 178)
color: 
(646, 179)
color: 
(646, 180)
color: 
(647, 178)
color: 
(647, 179)
color: 
(647, 180)
color: 
(648, 178)
color: 
(648, 179)
color: 
(648, 180)
received: 
(646, 180)
color: 
(646, 180)
color: 
(646, 181)
color: 
(646, 182)
color: 
(647, 180)
color: 
(647, 181)
color: 
(647, 182)
color: 
(648, 180)
color: 
(648, 181)
color: 
(648, 182)
received: 
(646, 182)
color: 
(646, 182)
color: 
(646, 183)
color: 
(646, 184)
color: 
(647, 182)
color: 
(647, 183)
color: 
(647, 184)
color: 
(648, 182)
color: 
(648, 183)
color: 
(648, 184)
received: 
(645, 183)
color: 
(645, 183)
color: 
(645, 184)
color: 
(645, 185)
color: 
(646, 183)
color: 
(646, 184)
color: 
(646, 185)
color: 
(647, 183)
color: 
(647, 184)
color: 
(647, 185)
received: 
(645, 184)
color: 
(645, 184)
color: 
(645, 185)
color: 
(645, 186)
color: 
(646, 184)
color: 
(646, 185)
color: 
(646, 186)
color: 
(647, 184)
color: 
(647, 185)
color: 
(647, 186)
received: 
(640, 188)
color: 
(640, 188)
color: 
(640, 189)
color: 
(640, 190)
color: 
(641, 188)
color: 
(641, 189)
color: 
(641, 190)
color: 
(642, 188)
color: 
(642, 189)
color: 
(642, 190)
received: 
(639, 189)
color: 
(639, 189)
color: 
(639, 190)
color: 
(639, 191)
color: 
(640, 189)
color: 
(640, 190)
color: 
(640, 191)
color: 
(641, 189)
color: 
(641, 190)
color: 
(641, 191)
received: 
(639, 190)
color: 
(639, 190)
color: 
(639, 191)
color: 
(639, 192)
color: 
(640, 190)
color: 
(640, 191)
color: 
(640, 192)
color: 
(641, 190)
color: 
(641, 191)
color: 
(641, 192)
received: 
(638, 191)
color: 
(638, 191)
color: 
(638, 192)
color: 
(638, 193)
color: 
(639, 191)
color: 
(639, 192)
color: 
(639, 193)
color: 
(640, 191)
color: 
(640, 192)
color: 
(640, 193)
received: 
(634, 198)
color: 
(634, 198)
color: 
(634, 199)
color: 
(634, 200)
color: 
(635, 198)
color: 
(635, 199)
color: 
(635, 200)
color: 
(636, 198)
color: 
(636, 199)
color: 
(636, 200)
received: 
(633, 199)
color: 
(633, 199)
color: 
(633, 200)
color: 
(633, 201)
color: 
(634, 199)
color: 
(634, 200)
color: 
(634, 201)
color: 
(635, 199)
color: 
(635, 200)
color: 
(635, 201)
received: 
(630, 203)
color: 
(630, 203)
color: 
(630, 204)
color: 
(630, 205)
color: 
(631, 203)
color: 
(631, 204)
color: 
(631, 205)
color: 
(632, 203)
color: 
(632, 204)
color: 
(632, 205)
received: 
(629, 205)
color: 
(629, 205)
color: 
(629, 206)
color: 
(629, 207)
color: 
(630, 205)
color: 
(630, 206)
color: 
(630, 207)
color: 
(631, 205)
color: 
(631, 206)
color: 
(631, 207)
received: 
(629, 207)
color: 
(629, 207)
color: 
(629, 208)
color: 
(629, 209)
color: 
(630, 207)
color: 
(630, 208)
color: 
(630, 209)
color: 
(631, 207)
color: 
(631, 208)
color: 
(631, 209)
received: 
(628, 208)
color: 
(628, 208)
color: 
(628, 209)
color: 
(628, 210)
color: 
(629, 208)
color: 
(629, 209)
color: 
(629, 210)
color: 
(630, 208)
color: 
(630, 209)
color: 
(630, 210)
received: 
(627, 209)
color: 
(627, 209)
color: 
(627, 210)
color: 
(627, 211)
color: 
(628, 209)
color: 
(628, 210)
color: 
(628, 211)
color: 
(629, 209)
color: 
(629, 210)
color: 
(629, 211)
received: 
(627, 211)
color: 
(627, 211)
color: 
(627, 212)
color: 
(627, 213)
color: 
(628, 211)
color: 
(628, 212)
color: 
(628, 213)
color: 
(629, 211)
color: 
(629, 212)
color: 
(629, 213)
received: 
(626, 213)
color: 
(626, 213)
color: 
(626, 214)
color: 
(626, 215)
color: 
(627, 213)
color: 
(627, 214)
color: 
(627, 215)
color: 
(628, 213)
color: 
(628, 214)
color: 
(628, 215)
received: 
(625, 215)
color: 
(625, 215)
color: 
(625, 216)
color: 
(625, 217)
color: 
(626, 215)
color: 
(626, 216)
color: 
(626, 217)
color: 
(627, 215)
color: 
(627, 216)
color: 
(627, 217)
received: 
(625, 217)
color: 
(625, 217)
color: 
(625, 218)
color: 
(625, 219)
color: 
(626, 217)
color: 
(626, 218)
color: 
(626, 219)
color: 
(627, 217)
color: 
(627, 218)
color: 
(627, 219)
received: 
(624, 219)
color: 
(624, 219)
color: 
(624, 220)
color: 
(624, 221)
color: 
(625, 219)
color: 
(625, 220)
color: 
(625, 221)
color: 
(626, 219)
color: 
(626, 220)
color: 
(626, 221)
received: 
(624, 221)
color: 
(624, 221)
color: 
(624, 222)
color: 
(624, 223)
color: 
(625, 221)
color: 
(625, 222)
color: 
(625, 223)
color: 
(626, 221)
color: 
(626, 222)
color: 
(626, 223)
received: 
(623, 221)
color: 
(623, 221)
color: 
(623, 222)
color: 
(623, 223)
color: 
(624, 221)
color: 
(624, 222)
color: 
(624, 223)
color: 
(625, 221)
color: 
(625, 222)
color: 
(625, 223)
received: 
(623, 220)
color: 
(623, 220)
color: 
(623, 221)
color: 
(623, 222)
color: 
(624, 220)
color: 
(624, 221)
color: 
(624, 222)
color: 
(625, 220)
color: 
(625, 221)
color: 
(625, 222)
received: 
(622, 219)
color: 
(622, 219)
color: 
(622, 220)
color: 
(622, 221)
color: 
(623, 219)
color: 
(623, 220)
color: 
(623, 221)
color: 
(624, 219)
color: 
(624, 220)
color: 
(624, 221)
received: 
(620, 215)
color: 
(620, 215)
color: 
(620, 216)
color: 
(620, 217)
color: 
(621, 215)
color: 
(621, 216)
color: 
(621, 217)
color: 
(622, 215)
color: 
(622, 216)
color: 
(622, 217)
received: 
(619, 213)
color: 
(619, 213)
color: 
(619, 214)
color: 
(619, 215)
color: 
(620, 213)
color: 
(620, 214)
color: 
(620, 215)
color: 
(621, 213)
color: 
(621, 214)
color: 
(621, 215)
received: 
(618, 212)
color: 
(618, 212)
color: 
(618, 213)
color: 
(618, 214)
color: 
(619, 212)
color: 
(619, 213)
color: 
(619, 214)
color: 
(620, 212)
color: 
(620, 213)
color: 
(620, 214)
received: 
(617, 210)
color: 
(617, 210)
color: 
(617, 211)
color: 
(617, 212)
color: 
(618, 210)
color: 
(618, 211)
color: 
(618, 212)
color: 
(619, 210)
color: 
(619, 211)
color: 
(619, 212)
received: 
(616, 207)
color: 
(616, 207)
color: 
(616, 208)
color: 
(616, 209)
color: 
(617, 207)
color: 
(617, 208)
color: 
(617, 209)
color: 
(618, 207)
color: 
(618, 208)
color: 
(618, 209)
received: 
(615, 205)
color: 
(615, 205)
color: 
(615, 206)
color: 
(615, 207)
color: 
(616, 205)
color: 
(616, 206)
color: 
(616, 207)
color: 
(617, 205)
color: 
(617, 206)
color: 
(617, 207)
received: 
(614, 204)
color: 
(614, 204)
color: 
(614, 205)
color: 
(614, 206)
color: 
(615, 204)
color: 
(615, 205)
color: 
(615, 206)
color: 
(616, 204)
color: 
(616, 205)
color: 
(616, 206)
received: 
(614, 203)
color: 
(614, 203)
color: 
(614, 204)
color: 
(614, 205)
color: 
(615, 203)
color: 
(615, 204)
color: 
(615, 205)
color: 
(616, 203)
color: 
(616, 204)
color: 
(616, 205)
received: 
(614, 202)
color: 
(614, 202)
color: 
(614, 203)
color: 
(614, 204)
color: 
(615, 202)
color: 
(615, 203)
color: 
(615, 204)
color: 
(616, 202)
color: 
(616, 203)
color: 
(616, 204)
received: 
(613, 201)
color: 
(613, 201)
color: 
(613, 202)
color: 
(613, 203)
color: 
(614, 201)
color: 
(614, 202)
color: 
(614, 203)
color: 
(615, 201)
color: 
(615, 202)
color: 
(615, 203)
received: 
(611, 195)
color: 
(611, 195)
color: 
(611, 196)
color: 
(611, 197)
color: 
(612, 195)
color: 
(612, 196)
color: 
(612, 197)
color: 
(613, 195)
color: 
(613, 196)
color: 
(613, 197)
received: 
(611, 194)
color: 
(611, 194)
color: 
(611, 195)
color: 
(611, 196)
color: 
(612, 194)
color: 
(612, 195)
color: 
(612, 196)
color: 
(613, 194)
color: 
(613, 195)
color: 
(613, 196)
received: 
(610, 191)
color: 
(610, 191)
color: 
(610, 192)
color: 
(610, 193)
color: 
(611, 191)
color: 
(611, 192)
color: 
(611, 193)
color: 
(612, 191)
color: 
(612, 192)
color: 
(612, 193)
received: 
(610, 190)
color: 
(610, 190)
color: 
(610, 191)
color: 
(610, 192)
color: 
(611, 190)
color: 
(611, 191)
color: 
(611, 192)
color: 
(612, 190)
color: 
(612, 191)
color: 
(612, 192)
received: 
(609, 189)
color: 
(609, 189)
color: 
(609, 190)
color: 
(609, 191)
color: 
(610, 189)
color: 
(610, 190)
color: 
(610, 191)
color: 
(611, 189)
color: 
(611, 190)
color: 
(611, 191)
received: 
(609, 186)
color: 
(609, 186)
color: 
(609, 187)
color: 
(609, 188)
color: 
(610, 186)
color: 
(610, 187)
color: 
(610, 188)
color: 
(611, 186)
color: 
(611, 187)
color: 
(611, 188)
received: 
(608, 185)
color: 
(608, 185)
color: 
(608, 186)
color: 
(608, 187)
color: 
(609, 185)
color: 
(609, 186)
color: 
(609, 187)
color: 
(610, 185)
color: 
(610, 186)
color: 
(610, 187)
received: 
(608, 182)
color: 
(608, 182)
color: 
(608, 183)
color: 
(608, 184)
color: 
(609, 182)
color: 
(609, 183)
color: 
(609, 184)
color: 
(610, 182)
color: 
(610, 183)
color: 
(610, 184)
received: 
(608, 178)
color: 
(608, 178)
color: 
(608, 179)
color: 
(608, 180)
color: 
(609, 178)
color: 
(609, 179)
color: 
(609, 180)
color: 
(610, 178)
color: 
(610, 179)
color: 
(610, 180)
received: 
(608, 177)
color: 
(608, 177)
color: 
(608, 178)
color: 
(608, 179)
color: 
(609, 177)
color: 
(609, 178)
color: 
(609, 179)
color: 
(610, 177)
color: 
(610, 178)
color: 
(610, 179)
received: 
(608, 175)
color: 
(608, 175)
color: 
(608, 176)
color: 
(608, 177)
color: 
(609, 175)
color: 
(609, 176)
color: 
(609, 177)
color: 
(610, 175)
color: 
(610, 176)
color: 
(610, 177)
received: 
(608, 174)
color: 
(608, 174)
color: 
(608, 175)
color: 
(608, 176)
color: 
(609, 174)
color: 
(609, 175)
color: 
(609, 176)
color: 
(610, 174)
color: 
(610, 175)
color: 
(610, 176)
received: 
(608, 171)
color: 
(608, 171)
color: 
(608, 172)
color: 
(608, 173)
color: 
(609, 171)
color: 
(609, 172)
color: 
(609, 173)
color: 
(610, 171)
color: 
(610, 172)
color: 
(610, 173)
received: 
(608, 169)
color: 
(608, 169)
color: 
(608, 170)
color: 
(608, 171)
color: 
(609, 169)
color: 
(609, 170)
color: 
(609, 171)
color: 
(610, 169)
color: 
(610, 170)
color: 
(610, 171)
received: 
(609, 168)
color: 
(609, 168)
color: 
(609, 169)
color: 
(609, 170)
color: 
(610, 168)
color: 
(610, 169)
color: 
(610, 170)
color: 
(611, 168)
color: 
(611, 169)
color: 
(611, 170)
received: 
(609, 167)
color: 
(609, 167)
color: 
(609, 168)
color: 
(609, 169)
color: 
(610, 167)
color: 
(610, 168)
color: 
(610, 169)
color: 
(611, 167)
color: 
(611, 168)
color: 
(611, 169)
received: 
(609, 166)
color: 
(609, 166)
color: 
(609, 167)
color: 
(609, 168)
color: 
(610, 166)
color: 
(610, 167)
color: 
(610, 168)
color: 
(611, 166)
color: 
(611, 167)
color: 
(611, 168)
received: 
(610, 165)
color: 
(610, 165)
color: 
(610, 166)
color: 
(610, 167)
color: 
(611, 165)
color: 
(611, 166)
color: 
(611, 167)
color: 
(612, 165)
color: 
(612, 166)
color: 
(612, 167)
received: 
(612, 164)
color: 
(612, 164)
color: 
(612, 165)
color: 
(612, 166)
color: 
(613, 164)
color: 
(613, 165)
color: 
(613, 166)
color: 
(614, 164)
color: 
(614, 165)
color: 
(614, 166)
received: 
(613, 164)
color: 
(613, 164)
color: 
(613, 165)
color: 
(613, 166)
color: 
(614, 164)
color: 
(614, 165)
color: 
(614, 166)
color: 
(615, 164)
color: 
(615, 165)
color: 
(615, 166)
received: 
(614, 164)
color: 
(614, 164)
color: 
(614, 165)
color: 
(614, 166)
color: 
(615, 164)
color: 
(615, 165)
color: 
(615, 166)
color: 
(616, 164)
color: 
(616, 165)
color: 
(616, 166)
received: 
(618, 164)
color: 
(618, 164)
color: 
(618, 165)
color: 
(618, 166)
color: 
(619, 164)
color: 
(619, 165)
color: 
(619, 166)
color: 
(620, 164)
color: 
(620, 165)
color: 
(620, 166)
received: 
(619, 164)
color: 
(619, 164)
color: 
(619, 165)
color: 
(619, 166)
color: 
(620, 164)
color: 
(620, 165)
color: 
(620, 166)
color: 
(621, 164)
color: 
(621, 165)
color: 
(621, 166)
received: 
(619, 165)
color: 
(619, 165)
color: 
(619, 166)
color: 
(619, 167)
color: 
(620, 165)
color: 
(620, 166)
color: 
(620, 167)
color: 
(621, 165)
color: 
(621, 166)
color: 
(621, 167)
received: 
(619, 166)
color: 
(619, 166)
color: 
(619, 167)
color: 
(619, 168)
color: 
(620, 166)
color: 
(620, 167)
color: 
(620, 168)
color: 
(621, 166)
color: 
(621, 167)
color: 
(621, 168)
received: 
(619, 167)
color: 
(619, 167)
color: 
(619, 168)
color: 
(619, 169)
color: 
(620, 167)
color: 
(620, 168)
color: 
(620, 169)
color: 
(621, 167)
color: 
(621, 168)
color: 
(621, 169)
received: 
(620, 167)
color: 
(620, 167)
color: 
(620, 168)
color: 
(620, 169)
color: 
(621, 167)
color: 
(621, 168)
color: 
(621, 169)
color: 
(622, 167)
color: 
(622, 168)
color: 
(622, 169)
received: 
(620, 168)
color: 
(620, 168)
color: 
(620, 169)
color: 
(620, 170)
color: 
(621, 168)
color: 
(621, 169)
color: 
(621, 170)
color: 
(622, 168)
color: 
(622, 169)
color: 
(622, 170)
received: 
(620, 169)
color: 
(620, 169)
color: 
(620, 170)
color: 
(620, 171)
color: 
(621, 169)
color: 
(621, 170)
color: 
(621, 171)
color: 
(622, 169)
color: 
(622, 170)
color: 
(622, 171)
received: 
(620, 170)
color: 
(620, 170)
color: 
(620, 171)
color: 
(620, 172)
color: 
(621, 170)
color: 
(621, 171)
color: 
(621, 172)
color: 
(622, 170)
color: 
(622, 171)
color: 
(622, 172)
received: 
(621, 171)
color: 
(621, 171)
color: 
(621, 172)
color: 
(621, 173)
color: 
(622, 171)
color: 
(622, 172)
color: 
(622, 173)
color: 
(623, 171)
color: 
(623, 172)
color: 
(623, 173)
received: 
(621, 173)
color: 
(621, 173)
color: 
(621, 174)
color: 
(621, 175)
color: 
(622, 173)
color: 
(622, 174)
color: 
(622, 175)
color: 
(623, 173)
color: 
(623, 174)
color: 
(623, 175)
received: 
(621, 174)
color: 
(621, 174)
color: 
(621, 175)
color: 
(621, 176)
color: 
(622, 174)
color: 
(622, 175)
color: 
(622, 176)
color: 
(623, 174)
color: 
(623, 175)
color: 
(623, 176)
received: 
(622, 174)
color: 
(622, 174)
color: 
(622, 175)
color: 
(622, 176)
color: 
(623, 174)
color: 
(623, 175)
color: 
(623, 176)
color: 
(624, 174)
color: 
(624, 175)
color: 
(624, 176)
received: 
(623, 174)
color: 
(623, 174)
color: 
(623, 175)
color: 
(623, 176)
color: 
(624, 174)
color: 
(624, 175)
color: 
(624, 176)
color: 
(625, 174)
color: 
(625, 175)
color: 
(625, 176)
'''

paint = paint.replace('\n', '')
paint = paint.replace(' ', '')
paint = paint.replace('color:', '')
paint = paint.replace('received:', '')
paint = paint.replace(')', '), ')
lst2 = list(paint.split(", "))


for elem in lst1:
    if elem not in lst2:
        print(elem + " not in lst1")
    else:
        print("ok")
