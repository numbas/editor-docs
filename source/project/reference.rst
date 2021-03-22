.. _projects:

Projects
********

Projects provide a way of collecting all your work on a particular topic or course and automatically granting access to your collaborators.

In the Numbas editor, every exam or question must belong to a single project. 
Your account always has at least one project - your workspace.
When you create a new exam or question, you will be asked which project you want to attach it to.  The default option is your workspace, but this guide will walk you through creating additional projects. 

If you're putting together content for a course you're teaching, it is a good idea to create a new project as a single gathering point for your material. 
A project is effectively a "fenced off" area of the editor where you can concentrate on just the material you want to work on, without having to wade through unrelated items.

Creating a new project
======================

.. image:: images/create_project.png
    :alt: The "create a new project" form.

Click on the :guilabel:`New` button at the top of the page, and then on :guilabel:`Project`.
You need to fill in some information about your new project:

* **A name for the project.**
  This should succinctly describe what the project is for, or what it contains.
* **A longer description of the project.** 
  You could include a link to your course homepage, or some information about the aims of the project.
* **A default language for content created in this project.**
  Any new exams created in this project will use this language by default.
* **A default licence for content created in this project.**
  Any new exams created in this project will have this licence attached by default.

The project home page
=====================

A project's home page shows a *timeline* of activity on the project, the list of members, and links to create new content or browse the project's existing content.

.. image:: images/project_homepage.png
    :alt: A project's homepage.

The timeline shows all activity on exams or questions belonging to the project and any attached comments.
Timeline items belonging to each project you are a member of will also be shown in your personal timeline on the editor homepage.

The cog icon at the top of the page takes you to the project's options page. 
On this page you can change any of the project's settings or, if you're the project's owner and it is not your personal workspace, delete it.


Finding content inside a project
================================

From the project homepage, click on either of the :guilabel:`Browse` links to see the questions or exams belonging to the project. 
You can narrow down your search by adding a query in the search bar at the top of the page, or selecting one of the filters.

.. image:: images/search.png
    :alt: A search inside a project.

Project settings
================

Click on the cog icon at the top-right of the page to change a project's settings.

.. _public-project:

If :guilabel:`Visible to non-members?` is ticked, the project and all of its **published** content will be visible to the general public.

Adding someone to a project
===========================

From the project's homepage, click on the settings icon at the top of the list of members to go to the member settings page. 
In the :guilabel:`Add a member` box, type the name of the person you want to invite.
If they don't have an account yet, type their email address; they will get an email asking them to create an account and afterwards they will be given access to your project immediately.

.. image:: images/add_member.png
    :alt: The project members form, in the process of adding a new member.

You can control what project members are allowed to do: if you select :guilabel:`Can view` then the user will be able to look at, comment on, and download all content in the project, but not change anything. 
If you select :guilabel:`Can edit`, then they will also be able to create new content or change existing content.
You can also give project members access to individual exams or questions using the access controls on their respective edit pages.

Changing or removing a project member's access
==============================================

From the project's homepage, click on the settings icon at the top of the list of members to go to the member settings page. 

.. image:: images/manage_members.png
    :alt: Changing a member's access to the project.

Change a project member's access rights by selecting an option from the dropdown next to their name.

To remove a user from the project, tick the checkbox corresponding to their name, then click the :guilabel:`Save changes` button.

Transferring ownership of a project to someone else
===================================================

The owner of a project has certain privileges which no other user does, such as deleting the project. 

To transfer ownership of a project to somebody else, go to the :guilabel:`Members` settings page and click on the :guilabel:`Transfer ownership` button, then enter the name of the person you'd like to transfer ownership to.
That user will become the owner of the project, and you will be given editing access to the project. 

Deleting a project
==================

To delete a project, you must be its owner.
You cannot delete your personal workspace.

.. warning::
    Only delete a project if you're absolutely sure you do not need it any more.
    Deleting a project is an irreversible action that will result in the loss of data belonging to the project. 

To delete a project, go to the project's :guilabel:`Options` page and click on the :guilabel:`Delete this project` button.

Questions and exams belonging to the project will be reassigned to their authors' personal workspaces, but any comments on the project's activity timeline will be deleted.
