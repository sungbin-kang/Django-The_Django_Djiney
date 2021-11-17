# Django - The Django Djiney Project

The Django Djitney is an train route management system. You can view, edit, update and delete lines, stops and stations.

The main <strong>routes</strong> app uses three fundamental models <code>Line</code>, <code>Station</code>, and <code>Stop</code>. Each models are viewed, edited, updated and deleted using base view classes from django.views.generic and django.views.generic.edit packages.

## Model Attribute
<ul>
    <li><code>Line</code>
        <ul>
            <li>name: name of the line</li>
        </ul>
    </li>
    <li><code>Station</code>
        <ul>
            <li>name: name of the station</li>
            <li>accessibility: whether the station has handicap access</li>
            <li>age: age of the station</li>
            <li>last cleaned date: last time the station was cleaned</li>
        </ul>
    </li>
    <li><code>Stops</code>
        <ul>
            <li>line: the line that has passes this stop</li>
            <li>station: the station that line passes</li>
            <li>stop_number: the unique stop number</li>
        </ul>
    </li>

</ul>

Please see requriements.txt for required packages.

<img src="/img/:home:.png" />