##jslipsum
const length = %filltext:name=field 1%
const sentences = [
    ‘Lorem ipsum dolor sit amet, consectetur adipiscing elit.’,
    ‘Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.’,
    ‘Sed convallis tristique sem.’,
    ‘ Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh.’,
    ‘Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Morbi lacinia molestie dui.’,
    ‘Donec lacus nunc, viverra nec, blandit vel, egestas et, augue.’,
    ‘Curabitur sit amet mauris. Morbi in dui quis est pulvinar ullamcorper. ‘,
    ‘Morbi in ipsum sit amet pede facilisis laoreet.’,
    ‘Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue eget diam’,
    ‘In scelerisque sem at dolor.’
];

var output = ‘’

for (i = 0; i < length; i++) { 
    const index =  Math.floor(Math.random() * Math.floor(9));
    output += sentences[i] + “ “;
}