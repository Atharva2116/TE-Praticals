const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = 3000;

mongoose.connect('mongodb://localhost:27017/student');
const db = mongoose.connection;

const StudentMarksSchema = new mongoose.Schema({
    Name: String,
    Roll_No: Number,
    WAD_Marks: Number,
    CC_Marks: Number,
    DSBDA_Marks: Number,
    CNS_Marks: Number,
    AI_Marks: Number
})

const StudentMarks = mongoose.model('studentmarks', StudentMarksSchema);

const students = [
    {
        Name: 'Athrva',
        Roll_No: 10,
        WAD_Marks: 40,
        CC_Marks: 60,
        DSBDA_Marks: 80,
        CNS_Marks: 90,
        AI_Marks: 100
    }, {
        Name: 'Parth',
        Roll_No: 11,
        WAD_Marks: 50,
        CC_Marks: 40,
        DSBDA_Marks: 80,
        CNS_Marks: 90,
        AI_Marks: 60
    }
];

db.once('open', async () => {
    console.log('Connected to db');
    try {
        await StudentMarks.insertMany(students);
    } catch (error) {
        console.error(error);
    }
});

app.use(express.json());



// Display total count of documents and List all the documents in browser
app.get('/total', async (req, res) => {
    try {
        const count = await StudentMarks.countDocuments();
        res.send(`Total count of students : ${count}`);
    } catch (error) {
        console.error(error)
        res.status(500).send('Interal server error')
    }
})

// List all documents
app.get('/list', async (req, res) => {
    try {
        const find = await StudentMarks.find();
        res.json(find);
    } catch (error) {
        console.error(error)
        res.status(500).send('Interal server error')
    }
})

// List names of students who got more than 20 marks in DSBDA Subject
app.get('/dsbda', async (req, res) => {
    try {
        const find = await StudentMarks.find({ DSBDA_Marks: { $gt: 20 } }, { Name: 1, _id: 0 });
        res.json(find);
    } catch (error) {
        console.error(error)
        res.status(500).send('Interal server error')
    }
})


// List names who got more than 25 marks in all subjects

app.get('/allsubjects', async (req, res) => {
    try {
        const find = await StudentMarks.find({
            $and: [
                { WAD_Marks: { $gt: 25 } },
                { CC_Marks: { $gt: 25 } },
                { DSBDA_Marks: { $gt: 25 } },
                { CNS_Marks: { $gt: 25 } },
                { AI_Marks: { $gt: 25 } }
            ]

        }, { Name: 1, _id: 0 }
        );
        res.json(find);
    } catch (error) {
        console.error(error)
        res.status(500).send('Interal server error')
    }
});

// List names who got less than 40 in both Maths and Science

app.get('/mathscience', async (req, res) => {
    try {
        const find = await StudentMarks.find({
            $or: [
                { WAD__Marks: { $lt: 40 } },
                { CC_Marks: { $lt: 40 } }
            ]
        }, { Name: 1, _id: 0 }
        );
        res.json(find);
    } catch (error) {
        console.error(error)
        res.status(500).send('Interal server error')
    }
});


// Update marks of specified students by 10
app.put('/update/:rn', async (req, res) => {
    const rollNo = req.params.rn;
    try {
        await StudentMarks.updateMany({ Roll_No: rollNo }, { $inc: { WAD_Marks: 10, CC_Marks: 10, DSBDA_Marks: 10, CNS_Marks: 10, AI_Marks: 10 } });
        res.send('Marks updated successfully');
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

// Remove specified student document from collection
app.delete('/remove/:rn', async (req, res) => {
    const rollNo = req.params.rn;
    try {
        await StudentMarks.findOneAndDelete({ Roll_No: rollNo });
        res.send('Document removed successfully');
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

app.get('/table', async (req, res) => {
    try {
        const find = await StudentMarks.find();

        let html = "<table border='1'><tr><th>Name</th> <th>WAD</th><th>CC</th><th>DSBDA</th><th>CNS</th><th>AI</th> </tr>";
        find.forEach( student=>{
            html+=`<tr><td>${student.Name}</td><td>${student.WAD_Marks}</td><td>${student.CC_Marks}</td><td>${student.DSBDA_Marks}</td><td>${student.CNS_Marks}</td> <td>${student.AI_Marks}</td>`
        });
        html+="</table>";
        res.send(html);
    } catch (error) {
        console.error(error)
        res.status(500).send('Interal server error')
    }
})  

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
